#!/bin/bash
#Sample Batch Job Script
#
#SBATCH --time=12:00:00			   # Job run time (hh:mm:ss)
#SBATCH --mail-user="fu5@illinois.edu"   # Email address to alert when job starts/finishes
#SBATCH --nodes=1			   # Number of nodes
#SBATCH --ntasks-per-node=1                # Number of cores per node
#SBATCH --job-name=fu5-shorten-oc              # Name of job
#SBATCH --account=25sp-cs598gck-eng          # Account
#SBATCH --partition=eng-instruction       # Parititon
#SBATCH --output=fu5_log%j               # output file name
#SBATCH --mem=600G

#run my script
awk -F, '$8 >= 2004 || NR==1' ../open_citations_curated.csv > short_2004_open_citations_curated.csv
#awk -F, '$8 >= 2008 || NR==1' open_citations_curated.csv > louvain/short_open_citations_curated.csv
#awk -F, '$8 >= 2019 || NR==1' open_citations_curated.csv > short_2019_open_citations_curated.csv
#awk -F, '$8 >= 2007 || NR==1' open_citations_curated.csv > short_2007_open_citations_curated.csv
