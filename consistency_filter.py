
# Input to this code is FASTQs (one for each sample) containing sRNA sequences that aligned to host or microbe genome.
# Output is one FASTA containing only the sRNAs with exact matches in every sample dataset.

# The approach of this version is to only retains a list of those found with an exact match in every
# sample through finding the intersection of sets of sRNAs created from each sample's fastq. Further refinement
# could include non-exact matches, especially those with an exact match but within a longer sequence - if necessary.

import pathlib
import time

from Bio import SeqIO

start_time = time.time()

# iterate through directory containing input files to find files and add paths to a list
input_dir = r"C:\Users\clauc\PycharmProjects\pythonProject\consistency_input_fqs"
sample_file_names = [f for f in pathlib.Path(input_dir).iterdir()]

quant_input = len(sample_file_names)

# open input files and parse into a list of sets (i.e. list of x samples each containing set of y sRNAs)
total_seqs = []
for sample_file in sample_file_names:
    seqs = []
    for record in SeqIO.parse(sample_file, "fastq"):
        seqs.append(str(record.seq))
    total_seqs.append(set(seqs))
# print(total_seqs)

# Find the intersection of all sample sets (i.e.only sRNAs in ALL)
consistent_seqs = total_seqs[0].intersection(*total_seqs)
min_seq = len(min(consistent_seqs))
max_seq = len(max(consistent_seqs))

print("Number of common sequences across all", quant_input, "input files: ", len(consistent_seqs))
print("Sequence lengths range from: ", min_seq, " to ", max_seq)

# Write back to fasta
with open("consistency_output.fa", 'w') as output:
    for seq in enumerate(consistent_seqs):
        output.write(">" + f"srna_target_candidate_{seq[0]+1}" + "\n" + seq[1] + "\n")

# report run time (for dev only)
end_time = time.time()

print("Time taken: ", end_time - start_time, "seconds")
