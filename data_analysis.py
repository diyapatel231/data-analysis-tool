import pandas as pd
import numpy as np

# Function to analyze the dataset
def analyze_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Display basic statistics
    print("Descriptive Statistics:")
    print(df.describe())

    # Display correlation matrix if there are numeric columns
    if df.select_dtypes(include=[np.number]).shape[1] > 1:
        print("\nCorrelation Matrix:")
        print(df.corr())
    else:
        print("\nNo numeric columns available for correlation analysis.")
