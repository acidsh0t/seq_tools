#! python3

import subprocess
import os
from configparser import ConfigParser
'''
Require flye to be installed and mapped to PATH to function
Requires python3 to be installed and mapped to PATH to function
Will ONLY work on long reads. Will automatically ignore short reads.
Assumes you are running on raw nanopore reads
<https://anaconda.org/bioconda/flye>
<https://github.com/fenderglass/Flye/>

##Instructions for use
Run 'python3 ../path/to/flye.py' in directory containing .fastq or filtlong/
For long read, '_' cannot be in file name

Input: All .fastq or fastq.gz in current directory. If filtlong/ in directory, will search sequences inside
Output: Folder(s) in current directory. If there is a filtlong/ directory, results will be in that directory
'''
config=ConfigParser()
config.read('config.ini')

threads=config.get('main','threads')

def main():
    long_list=[]
    for seq in os.listdir(): #groups sequences into short and long reads
        if seq.endswith('.fastq') or seq.endswith('fastq.gz'):
            if '_' not in seq:
                long_list.append(seq)
    n=0
    for seq in long_list:
        seq=long_list[n]
        flye='flye -o '+str(n)+'flye_plasmid --threads '+str(threads)+' --nano-raw '+seq+' --plasmid' #assumes it is reading raw nanopore reads
        print(flye)
        subprocess.call(flye,shell=True)                
        n=n+1

if __name__ == "__main__":
    main()