import numpy as np
import pandas

#load srna target sequences and parse into lists (which are ordered) for later data frame
with open("output.fa", 'r') as input:
    fasta = input.read().splitlines()

definitions = fasta[::2]
sequences = fasta[1::2]

lengths = [len(seq) for seq in sequences]

#use seqs as searches in each sample to find abundances (RPMs)

sample_names = ["LWH04", "LWH12", "LWH56", "LWH61"]
sample_file_paths = [r"./Batch_1_RPM/" + sample_name + r"_RPM.csv" for sample_name in sample_names]

# LWH04 = r".\Batch_1_RPM\LWH04_RPM.csv"
# LWH12 = r".\Batch_1_RPM\LWH12_RPM.csv"
# LWH56 = r".\Batch_1_RPM\LWH56_RPM.csv"
# LWH61 = r".\Batch_1_RPM\LWH61_RPM.csv"
# sample_file_paths = [LWH04, LWH12, LWH56, LWH61]

def find_abundances(sequences, sample_file_path):
    sample = pandas.read_csv(sample_file_path)
    small_rna = list(sample["Small RNA Sequence"])
    freq = sample["Frequency"]
    abundance = [freq[small_rna.index(sequence)] for sequence in sequences]
    return abundance

total_abundances = [find_abundances(sequences, sample_file_path) for sample_file_path in sample_file_paths]


results_df = pandas.DataFrame(total_abundances).T  # dataframe version of array
column_names = [sample_name + " Abundance" for sample_name in sample_names]
results_df.columns = column_names

#create a list of average abundances
average_abundances = [np.average(results_df.iloc[index, :]) for index in range(len(sequences))]

#create a list of standard devs
#print(np.std(total_abundances_df.iloc[0, :]))
std_devs = [np.std(results_df.iloc[index, :]) for index in range(len(sequences))]

#make full df
results_df.insert(0,"Sequence",sequences)
results_df.insert(1,"Length (nt)", lengths)
results_df["Average Abundance"] = average_abundances
results_df["Standard Deviation"] = std_devs

results_df = results_df.sort_values(by=["Average Abundance"], ascending=False)

#write df to new csv file
results_df.to_csv('results.csv')