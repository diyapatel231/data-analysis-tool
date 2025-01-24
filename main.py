from data_cleaning import clean_data
from data_analysis import analyze_data
from data_visualization import visualize_data
import argparse

# Main function to parse command-line arguments and execute tasks
def main():
    parser = argparse.ArgumentParser(description="Data Analysis Tool")
    parser.add_argument("file", help="Path to the dataset (CSV, JSON, or Excel)")
    parser.add_argument("--clean", action="store_true", help="Clean the dataset")
    parser.add_argument("--analyze", action="store_true", help="Perform statistical analysis")
    parser.add_argument("--visualize", action="store_true", help="Generate visualizations")
    args = parser.parse_args()

    # Load and process the dataset
    file_path = args.file

    # Clean the dataset
    if args.clean:
        clean_data(file_path)

    # Perform statistical analysis
    if args.analyze:
        analyze_data(file_path)

    # Generate visualizations
    if args.visualize:
        visualize_data(file_path)

if __name__ == "__main__":
    main()
