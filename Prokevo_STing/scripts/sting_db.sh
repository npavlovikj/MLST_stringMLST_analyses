#!/bin/bash

# Load HCC modules
# . /util/opt/lmod/lmod/init/profile
# export -f module
# module use /util/opt/hcc-modules/Common/
# module load anaconda
conda activate ProkEvo_dir/prokevo_sting

# db_util.py "$@"
db_util.py fetch --query "Salmonella enterica" --out_dir "sting_db_out" --build_index
tar -czvf sting_db_out.tar.gz sting_db_out
