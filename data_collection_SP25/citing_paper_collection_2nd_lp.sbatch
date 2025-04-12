#!/bin/bash
#Sample Batch Job Script
#
#SBATCH --time=12:00:00			   # Job run time (hh:mm:ss)
#SBATCH --mail-user="fu5@illinois.edu"   # Email address to alert when job starts/finishes
#SBATCH --nodes=1			   # Number of nodes
#SBATCH --ntasks-per-node=1                # Number of cores per node
#SBATCH --job-name=fu5-lp              # Name of job
#SBATCH --account=25sp-cs598gck-eng          # Account
#SBATCH --partition=eng-instruction       # Parititon
#SBATCH --output=fu5_log%j               # output file name
#SBATCH --mem=600G

#run my script
module load anaconda3/2024.10
source activate my.anaconda

echo "processing missing doi file"
python citing_paper_collection_2nd_lp.py "lp_1st_dois_missing.csv"
echo "end of processing missing doi file"

# echo "processing #5 file"
# python citing_paper_collection_2nd_lp.py "lp_1st_dois_5.csv"
# echo "end of processing #5 file"

# echo "processing #3 file"
# python citing_paper_collection_2nd_lp.py "lp_1st_dois_3.csv"
# echo "end of processing #3 file"

# did not finish
# echo "processing #1 file"
# python citing_paper_collection_2nd_lp.py "lp_1st_dois_1.csv"
# echo "end of processing #1 file"

