import joblib


def load_model(model_path):
    """
    Load a model from the given model path using joblib.

    Parameters:
    - model_path (str): Path to the saved model file.

    Returns:
    - model: Loaded model object.
    """
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print("Error loading the model:", e)
        return None
