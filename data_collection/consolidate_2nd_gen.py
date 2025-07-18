import pandas as pd
import os

def consolidate_csv_files(folder_path):

    all_files = []

    file_count = 0
    zero_citation_count = 0

    # Loop through all files in the directory
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            file_count += 1

            if df.shape[0] == 0:
                zero_citation_count += 1
            all_files.append(df)

    print("Total number of files: {}".format(file_count))
    print("Total number of files with zero_citations: {}".format(zero_citation_count))

    consolidated_df = pd.concat(all_files, ignore_index=True)

    return consolidated_df

def main():
    path_2nd = 'abeta/citation_2nd_gen'
    outfile_path = "my_data/consolidated/abeta_2nd.csv"
    citation_2nd = consolidate_csv_files(path_2nd)
    citation_2nd_missing_pub_year = consolidate_csv_files("abeta/missing_pub_year")
    citation_2nd = pd.concat([citation_2nd, citation_2nd_missing_pub_year], ignore_index=True)
    citation_2nd.to_csv(outfile_path, index=False)

    path_2nd = 'louvain/citation_2nd_gen'
    outfile_path = "my_data/consolidated/louvain_2nd.csv"
    citation_2nd = consolidate_csv_files(path_2nd)
    citation_2nd_missing_pub_year = consolidate_csv_files("louvain/missing_pub_year")
    citation_2nd = pd.concat([citation_2nd, citation_2nd_missing_pub_year], ignore_index=True)
    citation_2nd.to_csv(outfile_path, index=False)

    path_2nd = 'lp/citation_2nd_gen'
    outfile_path = "my_data/consolidated/lp_2nd.csv"
    citation_2nd = consolidate_csv_files(path_2nd)
    citation_2nd_missing_pub_year = consolidate_csv_files("lp/missing_pub_year")
    citation_2nd = pd.concat([citation_2nd, citation_2nd_missing_pub_year], ignore_index=True)
    citation_2nd.to_csv(outfile_path, index=False)

    path_2nd = 'gn/citation_2nd_gen'
    outfile_path = "my_data/consolidated/gn_2nd.csv"
    citation_2nd = consolidate_csv_files(path_2nd)
    citation_2nd_missing_pub_year = consolidate_csv_files("gn/missing_pub_year")
    citation_2nd = pd.concat([citation_2nd, citation_2nd_missing_pub_year], ignore_index=True)
    citation_2nd.to_csv(outfile_path, index=False)

if __name__ == "__main__":
    main()