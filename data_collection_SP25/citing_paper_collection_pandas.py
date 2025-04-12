import pandas as pd
import argparse

def main():

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Filter and save specific columns from a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output CSV file")
    parser.add_argument("target_string", help="String to search for in the third column")

    args = parser.parse_args()

    df = pd.read_csv(args.input_file)
    selection_df = df.loc[df['cited'] == args.target_string,]
    selection_df.to_csv(args.output_file, index=False)

if __name__ == '__main__':
    main()
