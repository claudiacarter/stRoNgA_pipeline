def read_fq_file(file_path):
    with open(file_path, 'r') as fq_file:
        lines = fq_file.readlines()
        return [(lines[i].strip(), lines[i+1].strip(), lines[i+3].strip()) for i in range(0, len(lines), 4)]

def write_fq_file(file_path, entries):
    """Writes a list of tuples (header, sequence, quality) to a FASTQ file."""
    with open(file_path, 'w') as fq_file:
        for entry in entries:
            fq_file.write(entry[0] + '\n' + entry[1] + '\n+\n' + entry[2] + '\n')

def remove_common_sequences(file1, file2, output_file1, output_file2):
    fq_entries_1 = read_fq_file(file1)
    fq_entries_2 = read_fq_file(file2)

    sequences_1 = set(entry[1] for entry in fq_entries_1)
    sequences_2 = set(entry[1] for entry in fq_entries_2)

    common_sequences = sequences_1.intersection(sequences_2)

    filtered_entries_1 = [entry for entry in fq_entries_1 if entry[1] not in common_sequences]
    filtered_entries_2 = [entry for entry in fq_entries_2 if entry[1] not in common_sequences]

    write_fq_file(output_file1, filtered_entries_1)
    write_fq_file(output_file2, filtered_entries_2)

    print(f"Common sequences removed. Results saved in {output_file1} and {output_file2}")

file1_path = ""                       # file path to sample's human-aligned reads in fq
file2_path = ""                       # file path to sample's Strongyloides-aligned reads in fq
output_file1_path = ""                # output file path for human-aligned reads minus common seqs
output_file2_path = ""                # output file path for Strongyloides-aligned reads minus common seqs

remove_common_sequences(file1_path, file2_path, output_file1_path, output_file2_path)
