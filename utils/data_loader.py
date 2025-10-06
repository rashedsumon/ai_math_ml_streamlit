import pandas as pd
import os

def load_salary_data():
    """
    Loads the Salary dataset safely, regardless of where the app is executed.
    Works on both local machines and Streamlit Cloud.
    """
    # Get the absolute path to the current file (utils/data_loader.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the dataset
    data_path = os.path.join(base_dir, "..", "data", "Salary_dataset.csv")
    data_path = os.path.normpath(data_path)  # Normalize path for cross-platform use

    # Check if the dataset exists
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"❌ Dataset not found at: {data_path}\n"
                                f"Make sure 'Salary_dataset.csv' is in the 'data/' folder.")

    # Load and return the dataset
    df = pd.read_csv(data_path)
    return df
