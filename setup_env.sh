#!/bin/bash

HOME_DIR=/data/$USER

# Source conda
source $HOME_DIR/miniconda3/etc/profile.d/conda.sh

# Create a new conda enviroment
conda create -n imo

# Activate the conda environment
conda activate imo

# Modify the configuration values in .condarc
conda config --env --add channels bioconda
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda config --env --add pinned_packages blas=*=mkl

# Update dependencies in the conda environment
conda env update -f environment.yml

