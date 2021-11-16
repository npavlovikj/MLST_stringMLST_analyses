#!/usr/bin/python

'''
NOTE:
- Comment out NCBI Download (sra_run) dependency line at the end if local Illumina sequences are used.
'''

import sys
import os

# Import the Python DAX library
os.sys.path.insert(0, "/usr/lib64/pegasus/python")
from Pegasus.DAX3 import *

dax = ADAG("pipeline")
base_dir = os.getcwd()

sra_run = []
sting_run = []
forward_file = []
reverse_file = []
list_of_sting_files = []


# Open input list and count files
input_file = open("sra_ids.txt")
lines = input_file.readlines()
input_file = open("sra_ids.txt")
length = len(input_file.readlines())

# Add file executable and job for sub-pipeline
c = File("sub-pipeline.dax")

# Add file for conda environment
conda_file = File("prokevo_sting.yml")


# Start analysis
# add job to create conda environment
conda_run = Job("ex_conda_run")
conda_run.addArguments(conda_file)
conda_run.uses(conda_file, link=Link.INPUT)
dax.addJob(conda_run)

# add job to create sting database
sting_db_run = Job("ex_sting_db_run")
sting_db_run.uses("sting_db_out.tar.gz", link=Link.OUTPUT, transfer=True)
dax.addJob(sting_db_run)

 
for i in range(0,length):

    srr_id = lines[i].strip()

    forward_file.append(File(str(srr_id) + "_1.fastq"))
    reverse_file.append(File(str(srr_id) + "_2.fastq"))
    dax.addFile(forward_file[i])
    dax.addFile(reverse_file[i])

    # add job for downloading data from NCBI
    sra_run.append(Job("ex_sra_run"))
    sra_run[i].addArguments(str(srr_id))
    sra_run[i].uses(forward_file[i], link=Link.OUTPUT, transfer=False)
    sra_run[i].uses(reverse_file[i], link=Link.OUTPUT, transfer=False)
    # add profile for download limit
    # Profile(PROPERTY_KEY[0], PROFILE KEY, PROPERTY_KEY[1])
    sra_run[i].addProfile(Profile("dagman", "CATEGORY", "sradownload"))
    # sra_run[i].addProfile(Profile("pegasus", "label", str(srr_id)))
    dax.addJob(sra_run[i])
     
    # add job for sting
    sting_run.append(Job("ex_sting_run"))
    sting_run[i].addArguments("sting_db_out.tar.gz", forward_file[i].name, reverse_file[i].name, str(srr_id))
    sting_run[i].uses(forward_file[i], link=Link.INPUT, transfer=False)
    sting_run[i].uses(reverse_file[i], link=Link.INPUT, transfer=False)
    sting_run[i].uses(str(srr_id) + "_salmonella.35.txt", link=Link.OUTPUT, transfer=True)
    dax.addJob(sting_run[i])
    f = File(str(srr_id) + "_salmonella.35.txt")
    list_of_sting_files.append(f)

# add job for cat sting files
ex_cat = Executable(namespace="dax", name="cat", version="4.0", os="linux", arch="x86_64", installed=True)
ex_cat.addPFN(PFN("/bin/cat", "local-hcc"))
dax.addExecutable(ex_cat)
output_sting_cat = File("sting_all.csv")
cat = Job(namespace="dax", name=ex_cat)
cat.addArguments(*list_of_sting_files)
for l in list_of_sting_files:
    cat.uses(l, link=Link.INPUT)
cat.setStdout(output_sting_cat)
cat.uses(output_sting_cat, link=Link.OUTPUT, transfer=True, register=False)
dax.addJob(cat)

# add job for sting output filtering
output_sting_merge_cat = File("sting_all_merge.csv")
merge_sting_run = Job("ex_merge_sting")
merge_sting_run.addArguments(output_sting_cat, output_sting_merge_cat)
merge_sting_run.uses(output_sting_cat, link=Link.INPUT)
merge_sting_run.uses(output_sting_merge_cat, link=Link.OUTPUT, transfer=True)
dax.addJob(merge_sting_run)


input_file = open("sra_ids.txt")
length = len(input_file.readlines())
dax.addDependency(Dependency(parent=conda_run, child=sting_db_run))
for i in range(0,length):
    # Add control-flow dependencies
    dax.addDependency(Dependency(parent=conda_run, child=sra_run[i]))
    dax.addDependency(Dependency(parent=sting_db_run, child=sting_run[i]))
    dax.addDependency(Dependency(parent=sra_run[i], child=sting_run[i]))
    dax.addDependency(Dependency(parent=sting_run[i], child=cat))
dax.addDependency(Dependency(parent=cat, child=merge_sting_run))


# Write the DAX to stdout
dax.writeXML(sys.stdout)
