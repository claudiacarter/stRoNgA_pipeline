# stRoNgA Pipeline
Finds small RNAs that make good diagnostic biomarkers in RNA-seq data. Developed by @claudiacarter and @Dropeza for the Hunt lab originally to help find exosomal small RNA biomarkers indicating human infection with _Strongyloides stercoralis_, but we are working on extending applicability to other host-parasite data.

To use this pipeline you will need (per sample):
1) fastq file of sRNAs aligned to the host genome
2) fastq file of sRNAs aligned to the parasite genome
3) The reads per million (RPM) for each sequence in CSV format; Column 1 containing sequence, Column 2 containing RPM (with headers)

The first two requirements are outputs of the Hunt Lab Small RNA Pipeline, the third will need preparation from the output *frequencies* by the following equation applied to each sequence:

RPM = (Sequence Frequency/Total Sequences)*10^6

The scripts are designed to filter the large number of small RNAs to a smaller number that are worth exploring more in-depth, e.g. for specificity.

Filtering Steps:\
1 - Remove sequences common to both host and parasite from each sample\
2 - Remove sequences that don't appear in every sample (applies to parasite-aligned fqs only)\
3 - Rank the remaining sequences by average abundance across the samples\

The user can establish their own cut-off for abundance and proceed to analyse the top candidates further, e.g. by BLAST to check specificity to the parasite.

PLEASE NOTE:
The tutorial ipython notebook, clustering.py and main.nf files are all part of future development and are not suitable for use at this time.

fastasplitter.py is an optional script if you need to chop up any of the fasta files into smaller files to perform BLAST or any other file size-limited task.
