# stRoNgA Pipeline
Finds small RNAs that make good diagnostic biomarkers in RNA-seq data. Developed by @claudiacarter and @Dropeza for the Vicky Hunt lab originally to help find exosomal small RNA biomarkers indicating human infection with _Strongyloides stercoralis_, but we are working on extending applicability to other host-parasite data.

This is a 4 part workflow, narrowing sequences of interest from an initial input of fastq files per sample per alignment containing only small RNAs that aligned to either host or parasite. There is fastq input/output at each stage for max flexibility.

Cross Referencing > Consistency > Abundance Ranking > Specificity
