import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate visualizations for the dataset
def visualize_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Example 1: Bar chart for categorical data
    if 'Department' in df.columns:
        df['Department'].value_counts().plot(kind='bar', color='skyblue')
        plt.title("Employees per Department")
        plt.ylabel("Count")
        plt.savefig("screenshots/bar_chart.png")
        plt.show()

    # Example 2: Scatter plot for numerical data
    if 'Age' in df.columns and 'Salary' in df.columns:
        sns.scatterplot(x='Age', y='Salary', data=df)
        plt.title("Age vs Salary")
        plt.savefig("screenshots/scatter_plot.png")
        plt.show()

    # Example 3: Correlation heatmap
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    if not numeric_cols.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Matrix")
        plt.savefig("screenshots/heatmap.png")
        plt.show()
