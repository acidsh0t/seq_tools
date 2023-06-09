#!/bin/bash

#run by executing "bash -i setup.sh"

#pandas
conda install -c conda-forge pandas

#filtlong
conda create -n filtlong -c bioconda filtlong

#unicycler
conda create -n unicycler -c bioconda unicycler

#flye
conda create -n flye -c bioconda flye

#raven
conda create -n raven -c bioconda raven-assembler

#abricate
conda create -n abricate -c bioconda abricate

#trim-galore
conda create -n trim-galore -c bioconda trim-galore

#bbmap
conda create -n bbmap -c bioconda bbmap

#seqkit
conda create -n seqkit -c bioconda seqkit

#bowtie
conda create -n bowtie -c bioconda bowtie2

#samtools
conda create -n samtools -c bioconda samtools=1.9

#subreads
conda create -n subread -c bioconda subread