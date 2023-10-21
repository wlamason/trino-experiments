#!/bin/bash

dataset_name=$1

if [[ ! -e ~/.kaggle/kaggle.json && ( -z "$KAGGLE_USERNAME" || -z "$KAGGLE_KEY" ) ]]
then
    echo "kaggle credentials do not exist"
    echo "follow instructions for kaggle.json or kaggle environment variables"
    echo "https://github.com/Kaggle/kaggle-api/tree/main"
else
    # https://github.com/Kaggle/kaggle-api/tree/main#download-dataset-files
    # Dataset URL suffix in format <owner>/<dataset-name>
    kaggle datasets download --path datasets --unzip $dataset_name
fi
