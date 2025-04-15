#!/bin/bash
#Sample Batch Job Script
#
#SBATCH --time=12:00:00			   # Job run time (hh:mm:ss)
#SBATCH --mail-user="fu5@illinois.edu"   # Email address to alert when job starts/finishes
#SBATCH --nodes=1			   # Number of nodes
#SBATCH --ntasks-per-node=1                # Number of cores per node
#SBATCH --job-name=fu5-louvain_induced_graph  # Name of job
#SBATCH --account=25sp-cs598gck-eng          # Account
#SBATCH --partition=eng-instruction       # Parititon
#SBATCH --output=fu5_log%j               # output file name
#SBATCH --mem=600G

#run my script
module load anaconda3/2024.10
source activate networkx
python induced_graph_construction.py "~/scratch/lp/short_2007_open_citations_curated.csv" "lp_selected_node_list.csv" "induced_graph_lp.json"

