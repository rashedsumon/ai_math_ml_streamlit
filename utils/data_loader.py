import pandas as pd
import os

def load_salary_data():
    data_path = os.path.join("data", "Salary_dataset.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}")
    return pd.read_csv(data_path)
