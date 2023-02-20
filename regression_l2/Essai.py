import numpy as np
import pandas as pd
from scipy import stats
import time
#import evcouplings
import glob

# Read in list of isolates
phenotypes =  pd.read_csv("../input_data/master_table_resistance.csv")
isolate_order = list(phenotypes.Isolate)

# Iterate through each fasta file, select only the positions with a high enough MAF
# Keep only the isolates with phenotype data, reorder the alignment to match isolate_order
# save a reduced fasta file
#mkdir fastas_reduced
path_to_fastas = "../input_data/fasta_files"
for f in glob.glob(f"{path_to_fastas}/*.fasta"):
    print(f)
