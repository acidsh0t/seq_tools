#! python3

import subprocess
import os

'''
Requires raven to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
Will ONLY work on long reads. Will automatically ignore short reads.
Assumes you are running on raw nanopore reads
<https://anaconda.org/bioconda/raven-assembler>
<https://github.com/lbcb-sci/raven>

##Instructions for use
Run 'python3 ../path/to/raven.py' in directory containing .fastq or filtlong/
For long read, '_' cannot be in file name

Input: All .fastq or fastq.gz in current directory. If filtlong/ in directory, will search sequences inside
Output: Folder(s) in current directory. If there is a filtlong/ directory, results will be in that directory
'''
def main():
    filtlong=False
    long_list=[]
    if os.path.isdir('filtlong'):
        filtlong=True
        os.chdir('filtlong') #makes filtlong/ current working directory
    for seq in os.listdir(): 
        if seq.endswith('.fastq') or seq.endswith('fastq.gz') and '_2' not in seq and '_1' not in seq: #ensure no short reads are added to list
            long_list.append(seq) #adds long-reads to list

    if len(long_list)>0:
        for seq in long_list:
            if filtlong==True:
                mkdir='mkdir ../raven'
                subprocess.call(mkdir,shell=True) 
                raven='raven --threads 8 '+seq+' > ../raven/assembly.fasta'
            else:
                mkdir='mkdir raven'
                subprocess.call(mkdir,shell=True) 
                raven='raven --threads 8 '+seq+' > raven/assembly.fasta'
            subprocess.call(raven,shell=True)                

if __name__ == "__main__":
    main()