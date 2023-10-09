#!/bin/bash
export DATA_FOLDER="/tmp/BOTNet-datasets"
git clone https://github.com/davkovacs/BOTNet-datasets.git $DATA_FOLDER
cd $DATA_FOLDER
git reset --hard 29e6d467317e4b5967b7ea5cbee54de953fa0d45
cd -