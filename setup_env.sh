#!/bin/bash

# Define your environment name and environment file
ENV_NAME="imo"
ENV_FILE="environment.yml"

# Initialize conda
conda init

# Modify configuration values in .condarc
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
conda

# Function to create a new environment
create_env() {
  echo "Creating environment..."
  conda env create -f $ENV_FILE
}

# Function to update the existing environment
update_env() {
  echo "Updating environment..."
  conda env update -f $ENV_FILE --prune
}

# If the environment exists, update the enviroment. If not, create the environment.
if conda info --envs | grep -q "$ENV_NAME"; then
  echo "Environment $ENV_NAME exists."
  update_env
else
  echo "Environment $ENV_NAME does not exist."
  create_env
fi

