import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    'churn_prediction_training',
    default_args=default_args,
    description='A DAG to train a churn prediction model',
    schedule_interval=timedelta(days=1),
)


# Data preprocessing task
def preprocess_data():
    # Load data
    data = pd.read_csv(os.path.abspath('/datasets/churn_data.csv'))

    # Preprocessing steps (example)
    X = data.drop(columns=['Churn'])
    y = data['Churn']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save preprocessed data
    joblib.dump((X_train, X_test, y_train, y_test), '/datasets/models/preprocessed_data.pkl')


preprocess_data_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)


# Model training task
def train_model():
    # Load preprocessed data
    X_train, X_test, y_train, y_test = joblib.load('/datasets/models/preprocessed_data.pkl')

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy}')

    # Print classification report
    print(classification_report(y_test, y_pred))

    # Save the trained model
    joblib.dump(model, '/datasets/models/churn_prediction_model.pkl')


train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

# Define task dependencies
preprocess_data_task >> train_model_task
