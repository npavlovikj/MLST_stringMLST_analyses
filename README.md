## Project:
Pavlovikj, N., Gomes-Neto, J.C., Deogun, J.S. and Benson, A.K., 2021. Systems-based approach for optimization of a scalable bacterial ST mapping assembly-free algorithm. bioRxiv.

## Repository organization:
This repository contains the scripts used to generate the analyses and figures in the paper. The input files for our analyses, as well as the generated outputs are stored [here](https://figshare.com/account/home#/projects/123940). The **Prokevo_STing** and **Prokevo_stringMLST** directories contain the modified code of our computational platform [ProkEvo](https://github.com/npavlovikj/prokevo) that includes [stringMLST](https://github.com/jordanlab/stringMLST) and [STing](https://github.com/jordanlab/STing). More information about its usage can be found [here](https://github.com/npavlovikj/ProkEvo/wiki). The **figures_code** directory contains the R code used to generate the figures in the paper. The **scripts** directory contains the scripts we used to run the analyses on [Crane, one of the supercomputers at University of Nebraska](https://hcc.unl.edu/docs/).

## Goal:
Multi-locus sequence typing (MLST) is a well-established and widely used genotyping technique that classifies bacterial genomes into sequence types (ST). ST-based classification provides useful and relevant genotypic units for epidemiological surveillance, population genetic analyses and evolutionary inference. The ST classification is usually inferred from seven loci that are found in the species, and isolates sharing alleles at five or more loci are more likely to be ancestrally related. ST-based classification usually depends on genome assembly that can be a limiting factor in efficient and real-time genotyping. The [stringMLST](https://github.com/jordanlab/stringMLST) algorithm uses kmer-based ST classification directly from Illumina paired-end reads that overcomes the computational bottleneck of using assemblies. However, stringMLST has not been broadly evaluated across data from multiple Public Health-related bacterial pathogenic species.

## Approach:
We systematically examined the performance of stringMLST across a phylogenetically diverse set of bacterial pathogens that are of primary interest to Public Health. Our systematic approach compared the accuracy of classifications using the [standard MLST program](https://github.com/tseemann/mlst) vs. stringMLST, as well as the computational and statistical performances, through the following steps:
1) narrow-scope comparative analyses across 4 phylogenetic distinct pathogens species;
2) further examination of algorithmic performance within a single ecologically diverse bacterial species;
3) wide-scope comparison between phylogenetic divergent pathogenic species with Public Health relevance and with databases available on [pubMLST](https://pubmlst.org/) for direct contrast between stringMLST and mlst.

## Results:
Based on the analyses performed in this work, three major findings are:
1) optimal kmer length for stringMLST is species-specific;
2) genome-intrinsic (number of contigs per genome, total number of nucleotides per genome, GC% content per genome, dinucleotide composition of genomes) and genome-extrinsic (total count of unique STs per database, total count of unique alleles across all seven loci) features can affect performance and accuracy of stringMLST;
3) implementing stringMLST in ProkEvo facilitates automated, reproducible bacterial population analyses.

## Implications:
stringMLST is an accurate, rapid and scalable tool for ST-based classification that uses raw reads and could be deployed in microbiological laboratories and epidemiological agencies for real-time surveillance and typing. stringMLST can be optimized across phylogenetic divergent species and populations of bacterial pathogens. There are three major implications or actionable knowledge that we propose: 
1) optimization of the kmer length for stringMLST in two ways:

    1.1. intrinsically by implementing a pre-step inside the algorithm to sample from the target data and select the optimal kmer length;
    
    1.2. by the user through a heuristic data mining approach to select the optimal kmer length prior to finalizing the ST calls.
2) using longer sequence reads has the potential to improve the accuracy of stringMLST for some bacterial species;
3) integrating stringMLST into computational platforms such as ProkEvo allows for utilizing various hierarchical genotyping strategies in a scalable and automated way. 
