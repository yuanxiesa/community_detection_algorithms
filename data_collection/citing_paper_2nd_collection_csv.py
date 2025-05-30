import csv
import os

def search_2nd_gen_citation(oc_file_path, case_name, doi_file, output_folder_path):

    # read the doi file
    with open(doi_file, 'r', encoding='utf-8') as f:
        doi_l = []
        user_id_l = []
        doi_dict = dict()
        reader = csv.reader(f, delimiter=',')
        header = next(reader)
        for row in reader:
            doi_l.append((row[1]))
            user_id_l.append(row[0])
            doi_dict[row[1]] = row[0]

    header_string = "oci,citing,cited,creation_date,time_span,journal_sc,author_sc,citing_pub_year,cited_pub_year\n"

    # create csv files in batch
    for user_id in user_id_l:
        outfile_path = os.path.join(output_folder_path, f"{user_id}.csv")
        with open(outfile_path, "w") as f:
            f.write(header_string)  # write in header

    # search oc files for the dois in the "cited" column (row[2])
    with open(oc_file_path) as oc:
        reader = csv.reader(oc)

        for row in reader:
            for doi in doi_l:
                doi = doi.strip()
                cited_doi = row[2].strip()
                if doi == cited_doi:
                    user_id = doi_dict[doi]
                    outfile_path = os.path.join(output_folder_path, f"{user_id}.csv")
                    with open(outfile_path, "a") as f:
                        f.write(",".join(row) + '\n')

def main():
    oc_file_path = 'missing_citing_pub_year.csv'
    case_name = 'abeta'
    doi_file = f'{case_name}_to_process.csv'
    output_folder_path = f'{case_name}_2nd_missing_pub_year'

    search_2nd_gen_citation(oc_file_path, case_name, doi_file, output_folder_path)

if __name__ == '__main__':
    main()