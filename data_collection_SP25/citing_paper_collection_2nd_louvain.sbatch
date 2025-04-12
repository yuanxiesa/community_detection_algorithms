#!/bin/bash
#Sample Batch Job Script
#
#SBATCH --time=12:00:00			   # Job run time (hh:mm:ss)
#SBATCH --mail-user="fu5@illinois.edu"   # Email address to alert when job starts/finishes
#SBATCH --nodes=1			   # Number of nodes
#SBATCH --ntasks-per-node=1                # Number of cores per node
#SBATCH --job-name=fu5-louvain-2nd              # Name of job
#SBATCH --account=25sp-cs598gck-eng          # Account
#SBATCH --partition=eng-instruction       # Parititon
#SBATCH --output=fu5_log%j               # output file name
#SBATCH --mem=600G

#run my script
module load anaconda3/2024.10
source activate my.anaconda

echo "processing missing doi file"
python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_missing.csv"
echo "end of processing missing doi file"

# echo "processing #18 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_18.csv"
# echo "end of processing #18 file"

# echo "processing #16 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_16.csv"
# echo "end of processing #16 file"

# echo "processing #14 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_14.csv"
# echo "end of processing #14 file"

# echo "processing #12 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_12.csv"
# echo "end of processing #12 file"

# echo "processing #10 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_10.csv"
# echo "end of processing #10 file"

# echo "processing #8 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_8.csv"
# echo "end of processing #8 file"

# echo "processing #6 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_6.csv"
# echo "end of processing #6 file"

# echo "processing #4 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_4.csv"
# echo "end of processing #4 file"

# echo "processing #2 file"
# python citing_paper_collection_2nd_louvain.py "louvain_1st_dir/louvain_1st_dois_2.csv"
# echo "end of processing #2 file"