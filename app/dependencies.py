# Dependency to provide access to the global variable
from fastapi import Request


def get_churn_model(request: Request):
    return request.app.state.churn_identifier
