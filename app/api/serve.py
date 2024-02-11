from datetime import datetime

from fastapi import APIRouter, Depends

from app.dependencies import get_churn_model
from app.models.input_data import InputData
from app.services.churn_service import ChurnPredictor
from app.helpers.logger import logger

serve_router = APIRouter()


# Simple GET endpoint
@serve_router.get("/hello")
def hello_world():
    return {"message": "Hello, world!"}


@serve_router.post("/is_customer_churn")
def predict_churn_api(data: InputData, model=Depends(get_churn_model)):
    """
    Endpoint to predict customer churn.

    Args:
    - data: InputData object containing input data.
    - model: Churn prediction model.

    Returns:
    - Prediction result or error message.
    """
    timestamp = datetime.now().isoformat()
    try:
        logger.info(f"Received data at {timestamp} for the CustomerId {data.customerID}")
        churn_predictor = ChurnPredictor(model)
        result = churn_predictor.predict_churn(data)
        return result
    except Exception as e:
        logger.error(f"Error for the input request at {timestamp} for the CustomerId {data.customerID} is {e}")
        return {"error": str(e)}
