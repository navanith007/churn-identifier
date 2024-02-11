import os

from app.helpers.utils import download_blob
from app.modules import load_model
from config import LOCAL_DESTINATION_MODEL_PATH, GCP_BUCKET_NAME, GCP_SOURCE_MODEL_PATH


def on_startup(app):
    # Create local directories if they don't exist
    # Create local directories if they don't exist
    local_directory = LOCAL_DESTINATION_MODEL_PATH.split('/')[0]
    os.makedirs(local_directory, exist_ok=True)

    download_blob(GCP_BUCKET_NAME, GCP_SOURCE_MODEL_PATH, LOCAL_DESTINATION_MODEL_PATH)

    model_path = os.path.abspath(LOCAL_DESTINATION_MODEL_PATH)

    app.state.churn_identifier = load_model(model_path=model_path)
