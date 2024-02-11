import pandas as pd


class ChurnPredictor:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def prepare_data(data):
        """
        Prepare input data into a pandas DataFrame.

        Args:
        - data: InputData object containing input data.

        Returns:
        - x_sample_test: Pandas DataFrame containing prepared data.
        """
        x_sample_test = pd.DataFrame(
            [{'tenure': data.tenure, 'TotalCharges': data.TotalCharges, 'OnlineSecurity': data.OnlineSecurity,
              'OnlineBackup': data.OnlineBackup, 'TechSupport': data.TechSupport,
              'Contract': data.Contract}])
        return x_sample_test

    def predict_churn(self, data):
        """
        Predict churn using the input data and model.

        Args:
        - data: InputData object containing input data.

        Returns:
        - result: Dictionary containing churn prediction results.
        """
        x_sample_test = self.prepare_data(data)
        is_churn = self.model.predict(x_sample_test)[0]
        probability = self.model.predict_proba(x_sample_test)[0][is_churn]
        return {'will_customer_churn': bool(is_churn), 'probability': float(probability)}
