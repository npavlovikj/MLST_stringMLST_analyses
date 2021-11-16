#!/bin/bash

# Load HCC modules
# . /util/opt/lmod/lmod/init/profile
# export -f module
# module use /util/opt/hcc-modules/Common/
# module load anaconda
conda activate ProkEvo_dir/prokevo_sting

# typer "$@"
tar xvf $1
typer -x ./sting_db_out/salmonella_enterica/db/index -1 $2 -2 $3 -s $4 -k 35 -y -o $4_salmonella.35.txt
