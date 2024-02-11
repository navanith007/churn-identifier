import json

import pandas as pd
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_churn_model

serve_router = APIRouter()


# Simple GET endpoint
@serve_router.get("/hello")
def hello_world():
    return {"message": "Hello, world!"}


class InputData(BaseModel):
    tenure: float
    TotalCharges: float
    OnlineSecurity: str
    OnlineBackup: str
    TechSupport: str
    Contract: str


# Endpoint to make predictions
@serve_router.post("/is_customer_churn")
def predict(data: InputData, model=Depends(get_churn_model)):
    print(data)
    X_sample_test = pd.DataFrame.from_dict(
        [{'tenure': data.tenure, 'TotalCharges': data.TotalCharges, 'OnlineSecurity': data.OnlineSecurity,
          'OnlineBackup': data.OnlineBackup, 'TechSupport': data.TechSupport,
          'Contract': data.Contract}])

    is_churn = model.predict(X_sample_test)[0]
    probability = model.predict_proba(X_sample_test)[0][is_churn]

    return {'will_customer_churn': bool(is_churn), 'probability': float(probability)}
