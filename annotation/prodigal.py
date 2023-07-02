#! python3

##NOT READY

import os
import shutil
import subprocess

def main():
    try:
        shutil.rmtree('prodigal')
    except:
        pass
    os.mkdir('prodigal')

    for file in os.listdir(): #need to adjust to point to proper directory
        genes=file.replace('.fasta','_genes.fasta') #protein output
        prot=file.replace('.fasta','_prot.fasta') #protein output
        nuc=file.replace('.fasta','_nuc.fasta') #nucleotide output

        prodigal= 'prodigal -i '+file+' -o prodigal/'+genes+' -a '+prot+' -d '+nuc #outputs all to prodigal/
        try:
            subprocess.call(prodigal,shell=True)
        except:
            print('Something went wrong running prodigal on'+file)
            continue

if __name__=="__main__":
    main()