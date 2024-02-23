#!/usr/bin/env nextflow

//Declare syntax version
nextflow.enable.dsl = 2

//define where results are output
resultsdir = "results/"

// workflow for filtering sRNAs that have aligned to human (host) and/or S. stercoralis (parasite) genomes to a
// non-redundant list of target candidates for an sRNA to explore as a diagnostic biomarker

//Script params?
//params.query = "input directory path"
//params.db = "db path"

workflow {
// open a new channel to get input files (i.e. the small RNA pipeline sort output
ch_input = Channel
	.fromPath (".data/input/*.fq)
//define workflow

CONCATENATE (
//needs work! Bernie concatenation method but automated?
input: ch_input

output: 
)

REMOVE_COMMON (
input: CONCATENATE.out
)

CONSISTENCY_FILTER (

)

ABUNDANCE (
// searches the output of consistency filter against RPM output of small RNA pipeline and generates a CSV detailing
// abundances for each sample, average abundance (sort order) and standard deviation

)

FASTA_SPLIT (
// take the fasta output of abundance and split into multiple files of 50 seqs or less (maintaining abundance
// sort order)

)

CHUNKED_BLAST (

)

}



process CONCATENATE {

}

process REMOVE_COMMON {

}

process CONSISTENCY_FILTER {

}

process ABUNDANCE {

}

process CHUNKED_BLAST {

}