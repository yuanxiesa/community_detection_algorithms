import requests
import pandas as pd

def fill_year(df, year_col, doi_col, headers):

    base_url = "https://api.openalex.org/works"

    need_process = df.loc[df[year_col].isna()]
    print("{} DOIs need to be processed".format(len(need_process)))
    dois = list(need_process[doi_col])

    results = {}

    for doi in dois:
        doi = doi.lower().strip()
        url = f"{base_url}/https://doi.org/{doi}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            year = data.get("publication_year", "N/A")
            results[doi] = year
        else:
            results[doi] = f"Error {response.status_code}"

    for idx, row in df[df[year_col].isna()].iterrows():
        doi = row[doi_col]
        df.loc[idx, year_col] = results[doi]

    return df


def main():
    headers = {
        "User-Agent": "fetch_year (mailto:yuanxiesa@gmail.com)"  # optional but recommended
    }

    input_file_path = "V1/abeta_2nd.csv"
    output_file_path = "V2/abeta_2nd_year_ammended.csv"

    df = pd.read_csv(input_file_path)
    print('amending citing pub year ...')
    df = fill_year(df, 'citing_pub_year', "citing", headers)
    print('amending cited pub year ...')
    df = fill_year(df, 'cited_pub_year', "cited", headers)
    print('saving files')
    df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    main()