import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description="Filter and save specific columns from a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("oc_file", help="Path to the shortened oc CSV file")
    parser.add_argument("output_dir", help="Path to the output directory")
    args = parser.parse_args()

    oc = pd.read_csv(args.oc_file)
    doi_df = pd.read_csv(args.input_file)
    for row in doi_df.itertuples(index=True, name="Row"):
        prefix = row[1]
        doi = row[2]
        selection_df = oc.loc[oc['cited'] == doi,]
        outfile = f'{args.output_dir}/{prefix}.csv'
        selection_df.to_csv(outfile, index=False)
        
if __name__ == '__main__':
    main()
