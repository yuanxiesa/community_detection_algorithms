import pandas as pd

def main():

    oc = pd.read_csv('short_2019_open_citations_curated.csv')
    doi_df = pd.read_csv('leiden_1st_dois.csv')
    for row in doi_df.itertuples(index=True, name="Row"):
        prefix = row[1]
        doi = row[2]
        selection_df = oc.loc[oc['cited'] == doi,]
        outfile = f'{prefix}.csv'
        selection_df.to_csv(outfile, index=False)

if __name__ == '__main__':
    main()
