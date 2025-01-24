import pandas as pd

# Function to clean the dataset
def clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    print("Initial Dataset Info:")
    print(df.info())

    # Fill missing values with forward fill
    df.fillna(method='ffill', inplace=True)

    # Save the cleaned dataset to a new file
    cleaned_file = file_path.replace(".csv", "_cleaned.csv")
    df.to_csv(cleaned_file, index=False)
    print(f"Cleaned dataset saved to {cleaned_file}")
