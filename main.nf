#!/usr/bin/env nextflow

//Declare syntax version
nextflow.enable.dsl = 2

//define where results are output
resultsdir = "results/"

// workflow for filtering sRNAs that have aligned to human (host) and/or S. stercoralis (parasite) genomes to a non-redundant list of target candidates for an sRNA to explore as a diagnostic biomarker

//Script params?
//params.query = "input directory path"
//params.db = "db path"

workflow {
// open a new channel to get input files
ch_input = Channel
	.fromPath (".data/input/*.fq)
//define workflow

CONCATENATE (
//needs work!
)

REMOVE_COMMON (
CONCATENATE.out
)

CONSISTENCY_FILTER (

)

ABUNDANCE (

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