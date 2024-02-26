import matplotlib.pyplot as plt
import numpy as np
import pandas
import seaborn
from Levenshtein import distance
from sklearn.cluster import DBSCAN


def create_lev_matrix(ordered_list):
    array = np.zeros((len(ordered_list), len(ordered_list)), dtype=np.int64)
    for i in range(0, len(ordered_list)):
        for j in range(0, len(ordered_list)):
            array[i, j] = distance(ordered_list[i], ordered_list[j])
    return array

with open("results.fa", 'r') as input:
    fasta = input.read().splitlines()

definitions = fasta[::2]
sequences = fasta[1::2]

lev_matrix = create_lev_matrix(sequences)

eps = 3
min_samples = 2
dbscan = DBSCAN(metric="precomputed", eps=eps, min_samples=min_samples)
clusters = dbscan.fit_predict(lev_matrix)

# build a dataframe to organise sequences in clustered order
clustered_seqs = {
    "Cluster": clusters,
    "Sequence": sequences
                  }
# create datadrame and sort by cluster
unordered_df = pandas.DataFrame(clustered_seqs)
byclusters_df = unordered_df.sort_values(by=["Cluster"])

# sequences in cluster order to list for new heatmap
ordered_seqs = byclusters_df["Sequence"].tolist()

# generate heatmaps
#unordered = seaborn.heatmap(create_lev_matrix(sequences))
#plt.show()

ordered = seaborn.heatmap(create_lev_matrix(ordered_seqs))
plt.show()

# write df to new csv file
byclusters_df.to_csv('clustering_results.csv')