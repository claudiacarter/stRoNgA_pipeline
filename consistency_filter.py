
# Input to this code is FASTQs (one for each sample) containing sRNA sequences that
# aligned to host or microbe genome. Output is one FASTQ containing only the sRNAs with
# exact matches in every sample dataset.

# This version searches each sRNA found in any sample against each of the samples' sRNA sequences
# and only retains a list of those found with an exact match in every sample. Further refinement
# could include non-exact matches, especially those with an exact match but within a longer sequence.

from Bio import SeqIO

# open FASTQs and parse into a list of sets (i.e. list of x samples each containing set of y sRNAs)

# def read_fq_file(file_path):
#    with open(file_path, 'r') as fq_file:
#        lines = fq_file.readlines()
#        return [(lines[i].strip(), lines[i+1].strip(), lines[i+3].strip()) for i in range(0, len(lines), 4)]
test_sample_1 = "testsample1.fq"
test_sample_2 = "testsample2.fq"
test_sample_3 = "testsample3.fq"
sample_file_names = [test_sample_1, test_sample_2, test_sample_3]

total_seqs = []
for sample in sample_file_names:
    seqs = []
    for record in SeqIO.parse(sample, "fastq"):
        seqs.append(record.seq)
    total_seqs.append(set(seqs))
# print(total_seqs)

# Find the intersection of all sample sets (i.e.only sRNAs in ALL)

consistent_seqs = total_seqs[0].intersection(*total_seqs)
print(consistent_seqs)

# Write back to fasta/fastq, maybe include Abundance Ranking in here to return results in RPM order?
