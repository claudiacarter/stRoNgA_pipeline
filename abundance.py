import numpy as np
import pandas

def find_abundances(sequences, sample_file_path):
    sample = pandas.read_csv(sample_file_path)
    small_rna = list(sample["Small RNA Sequence"])
    freq = sample["RPM"]
    abundance = [freq[small_rna.index(sequence)] for sequence in sequences]
    # abundance = []
    # for sequence in sequences:
    #     try:
    #         abundance.append(freq[small_rna.index(sequence)])
    #         print(sequence, ' is found in ', sample_file_path)
    #     except:
    #         abundance.append(0)
    #         print(sequence, ' could not be found in ', sample_file_path)
    return abundance

# set up
batch = "Batch_1"
sample_names = ["LWH04", "LWH12", "LWH56", "LWH61"]
# Unused Sample Names: "LWH04", "LWH12", "LWH56", "LWH61", "CKH21", "CKH130", "KKU01", "LWH76"

# load sRNA consistent sequences and parse into lists (which are ordered) for later data frame
with open("consistency_output.fa", 'r') as input:
    fasta = input.read().splitlines()

definitions = fasta[::2]
sequences = fasta[1::2]

lengths = [len(seq) for seq in sequences]

# use seqs as searches in each sample to find abundances (i.e. frequencies/RPMs)
sample_file_paths = [r"./" + batch + r"_RPM/" + sample_name + r"_RPM.csv" for sample_name in sample_names]

total_abundances = [find_abundances(sequences, sample_file_path) for sample_file_path in sample_file_paths]

results_df = pandas.DataFrame(total_abundances).T  # dataframe version of array
column_names = [sample_name + " Abundance" for sample_name in sample_names]
results_df.columns = column_names

#create a list of averaged abundances
average_abundances = [np.average(results_df.iloc[index, :]) for index in range(len(sequences))]

#create a list of standard devs
std_devs = [np.std(results_df.iloc[index, :]) for index in range(len(sequences))]

#make full df
results_df.insert(0,"Definition Lines", definitions)
results_df.insert(1,"Sequence",sequences)
results_df.insert(2,"Length (nt)", lengths)
results_df["Average Abundance"] = average_abundances
results_df["Standard Deviation"] = std_devs

results_df = results_df.sort_values(by=["Average Abundance"], ascending=False)

# write df to new csv file
results_df.to_csv(f'abundance_results_{batch}.csv')

# write sequences in abundance descending order to a new fasta
ordered_deflines = results_df["Definition Lines"].tolist()
ordered_sequences = results_df["Sequence"].tolist()

with open(f"abundance_results_{batch}.fa", 'w') as output:
    for index, sequence in enumerate(ordered_sequences):
        output.write(f"{ordered_deflines[index]}" + "\n" + f"{ordered_sequences[index]}" + "\n")