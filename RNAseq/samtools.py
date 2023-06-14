#! python3

import os
import subprocess

threads=8

def bam():
    try:
        os.mkdir('BAM')
    except:
        pass

    for sam in os.listdir('Bowtie2_SAM'):
        bam=sam.replace('.sam','')
        samtools='samtools view -bS Bowtie2_SAM/'+sam+' -@ '+str(threads)+' > BAM/'+bam+'.bam'
        print(samtools)
        subprocess.call(samtools,shell=True)

def sort():
    for bam in os.listdir('BAM'):
        _sorted=bam.replace('.bam','_sorted.bam')
        sort='samtools sort BAM/'+bam+' -@ '+str(threads)+' -o '+_sorted
        print(sort)
        subprocess.call(sort,shell=True)

def index():
    sorted_list=[]
    for file in os.listdir():
        if file.endswith('_sorted.bam'):
            sorted_list.append(file)
    for _sorted in sorted_list:
        _index='samtools index '+_sorted+' -@ '+str(threads)
        print(_index)
        subprocess.call(_index,shell=True)

if __name__ == "__main__":
    bam()
    sort()
    index()