import requests

import pandas as pd
import requests
import time


def get_publication_year(doi, email):
    base_url = "https://api.openalex.org/works/https://doi.org/"
    headers = {"User-Agent": email}  # Replace with your email per OpenAlex polite policy

    try:
        response = requests.get(base_url + doi, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("publication_year", None)
    except Exception as e:
        print(f"Error for DOI {doi}: {e}")
    return None


def fill_missing_publication_years(df, doi_col, year_col, email, delay=1):
    """
    Fill missing publication years in a dataframe using OpenAlex and DOI lookup.

    Parameters:
        df (pd.DataFrame): The dataframe to update
        doi_col (str): Name of the column containing DOIs
        year_col (str): Name of the column to store publication years
        delay (float): Delay in seconds between API requests
    """
    for idx, row in df[df[year_col].isnull()].iterrows():
        doi = row[doi_col]
        if pd.notnull(doi):
            year = get_publication_year(doi, email)
            df.at[idx, year_col] = year
            print(f"Filled doi {doi} with year {year}")
            time.sleep(delay)  # polite delay between requests
    return df


def main():

    # processing 2nd-gen citations
    # df = pd.read_csv("my_data/consolidated/abeta_2nd.csv")
    # email = 'yuanxiesa@gmail.com'
    # print("processing citing dois")
    # df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    # print("processing cited dois")
    # df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    # df.to_csv("my_data/citation_2nd_pub_year_filled/abeta_2nd_missing_pub_year_filled.csv", index=False)

    # df = pd.read_csv("my_data/consolidated/louvain_2nd.csv")
    # email = 'yuanxiesa@gmail.com'
    # print("processing citing dois")
    # df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    # print("processing cited dois")
    # df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    # df.to_csv("my_data/citation_2nd_pub_year_filled/louvain_2nd_missing_pub_year_filled.csv", index=False)

    # df = pd.read_csv("my_data/consolidated/gn_2nd.csv")
    # email = 'yuanxiesa@gmail.com'
    # print("processing citing dois")
    # df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    # print("processing cited dois")
    # df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    # df.to_csv("my_data/citation_2nd_pub_year_filled/gn_2nd_missing_pub_year_filled.csv", index=False)

    # df = pd.read_csv("my_data/consolidated/lp_2nd.csv")
    # email = 'yuanxiesa@gmail.com'
    # print("processing citing dois")
    # df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    # print("processing cited dois")
    # df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    # df.to_csv("my_data/citation_2nd_pub_year_filled/lp_2nd_missing_pub_year_filled.csv", index=False)

    # processing 1st-gen citations
    # df = pd.read_csv("my_data/citation_1st/abeta_1st.csv")
    # email = 'yuanxiesa@gmail.com'
    # print("processing citing dois")
    # df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    # print("processing cited dois")
    # df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    # df.to_csv("my_data/citation_1st_pub_year_filled/abeta_1st_missing_pub_year_filled", index=False)

    # df = pd.read_csv("my_data/citation_1st/louvain_1st.csv")
    # email = 'yuanxiesa@gmail.com'
    # print("processing citing dois")
    # df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    # print("processing cited dois")
    # df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    # df.to_csv("my_data/citation_1st_pub_year_filled/louvain_1st_missing_pub_year_filled", index=False)

    # df = pd.read_csv("my_data/citation_1st/gn_1st.csv")
    # email = 'yuanxiesa@gmail.com'
    # print("processing citing dois")
    # df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    # print("processing cited dois")
    # df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    # df.to_csv("my_data/citation_1st_pub_year_filled/gn_1st_missing_pub_year_filled", index=False)

    df = pd.read_csv("my_data/citation_1st/lp_1st.csv")
    email = 'yuanxiesa@gmail.com'
    print("processing citing dois")
    df = fill_missing_publication_years(df, 'citing', 'citing_pub_year', email)
    print("processing cited dois")
    df = fill_missing_publication_years(df, 'cited', 'cited_pub_year', email)
    df.to_csv("my_data/citation_1st_pub_year_filled/lp_1st_missing_pub_year_filled", index=False)


if __name__ == "__main__":
    main()