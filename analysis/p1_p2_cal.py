import pandas as pd
import os
import argparse

def main():

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="perform cocitation analysis")
    parser.add_argument("first_gen_file", help="Path to the first generation citation, one csv")
    parser.add_argument("second_gen_file", help="Path to the second generation citation, one csv")
    parser.add_argument("output_file", help="Path to the output file")

    args = parser.parse_args()

    df_1st = pd.read_csv(args.first_gen_file)
    df_2nd = pd.read_csv(args.second_gen_file)

    year_l = list(df_2nd['citing_pub_year'].unique()) # collect all possible years from 2nd-gen citations
    year_l.sort()

    percent_l_1st = []
    percent_l_2nd = []
    doi_l = []

    n_total_2nd_doi = []
    n_total_1st_doi = []
    n_cocitation_doi = []

    for year in year_l:

        print(year)

        set_1st = set(df_1st.loc[df_1st['citing_pub_year'] == year, 'citing'])
        set_2nd = set(df_2nd.loc[df_2nd['citing_pub_year'] == year, 'citing'])


        n_total_1st_doi.append(len(set_1st))
        n_total_2nd_doi.append(len(set_2nd))
        n_cocitation_doi.append(len(set_1st.intersection(set_2nd)))

        percent_1st = round(len(set_1st.intersection(set_2nd)) / len(set_1st) * 100, 2)
        percent_2nd = round(len(set_1st.intersection(set_2nd)) / len(set_2nd) * 100, 2)
        doi_l.append(list(set_1st.intersection(set_2nd)))
        percent_l_1st.append(percent_1st)
        percent_l_2nd.append(percent_2nd)

    df_result = pd.DataFrame({

        'year': year_l,
        'percent 1st gen': percent_l_1st,
        'percent 2nd gen': percent_l_2nd,
        'cocitation_dois': doi_l,
        'n_total_1st_doi': n_total_1st_doi,
        'n_total_2nd_doi': n_total_2nd_doi,
        'n_cocitation_doi': n_cocitation_doi,
    })

    df_result.to_csv(args.output_file, index=False)

if __name__ == '__main__':
    main()