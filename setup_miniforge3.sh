#!/bin/bash

HOME_DIR=/data/$USER

curl -L -o "$HOME_DIR/Miniforge3-$(uname)-$(uname -m).sh" "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash $HOME_DIR/Miniforge3-$(uname)-$(uname -m).sh -b -u -p $HOME_DIR/miniforge3
rm -rf $HOME_DIR/Miniforge3-$(uname)-$(uname -m).sh

