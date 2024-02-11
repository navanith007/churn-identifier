from pydantic import BaseModel


class InputData(BaseModel):
    customerID: str
    tenure: int
    TotalCharges: float
    OnlineSecurity: str
    OnlineBackup: str
    TechSupport: str
    Contract: str
