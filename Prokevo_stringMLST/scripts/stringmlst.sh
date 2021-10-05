#!/bin/bash

# Load HCC modules
# . /util/opt/lmod/lmod/init/profile
# export -f module
# module use /util/opt/hcc-modules/Common/
# module load anaconda
conda activate ProkEvo_dir/prokevo_stringmlst

# stringMLST.py "$@"
tar xvf $1
stringMLST.py --predict -1 $2 -2 $3 -p -r -t -x -P ./salmonella_35/Salmonella_enterica -k 35 -o $4_salmonella.35.txt
