import pandas as pd

def main():

    input_fil_path = "my_data/original/abeta_1st.csv"
    output_file_path = "abeta_1st_doi.csv"

    df = pd.read_csv(input_fil_path)

    doi_l = list(df['citing'])
    doi_df = pd.DataFrame({"user_id": range(1, len(df) + 1), "doi": doi_l})
    doi_df.to_csv(output_file_path, index=False)

if __name__ == '__main__':
    main()