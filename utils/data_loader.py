import pandas as pd
import os

def load_salary_data():
    """
    Loads the Salary dataset safely, compatible with local and cloud environments.
    """
    # Get absolute path to current script (utils/data_loader.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Point to datasets/Salary_dataset.csv (based on your structure)
    data_path = os.path.join(base_dir, "..", "datasets", "Salary_dataset.csv")
    data_path = os.path.normpath(data_path)

    # Debug info (optional during testing)
    print(f"DEBUG: Looking for dataset at -> {data_path}")
    print(f"DEBUG: Current working directory -> {os.getcwd()}")

    # Raise error if not found
    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"❌ Dataset not found at: {data_path}\n"
            f"Make sure 'Salary_dataset.csv' is inside the 'datasets/' folder."
        )

    # Load dataset
    df = pd.read_csv(data_path)
    return df
