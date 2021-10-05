#!/bin/bash

# Load HCC modules
# . /util/opt/lmod/lmod/init/profile
# export -f module
# module use /util/opt/hcc-modules/Common/
# module load anaconda
conda activate ProkEvo_dir/prokevo_stringmlst

# stringMLST.py "$@"
stringMLST.py --getMLST --species="Salmonella enterica" -P "salmonella_35" -k 35
tar -czvf salmonella_35.tar.gz salmonella_35
