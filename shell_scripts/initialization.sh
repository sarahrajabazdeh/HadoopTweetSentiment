#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path="$1"

# # Check if the file path provided exists
if [ ! -f "$file_path" ]; then
    echo "Error: File '$file_path' does not exist."
    exit 1
fi

# This script is used to initialize the HDFS file system
hadoop fs -test -d user || hadoop fs -mkdir user
hadoop fs -test -d user/data || hadoop fs -mkdir user/data
hadoop fs -test -d user/data/kaggle || hadoop fs -mkdir user/data/kaggle
hadoop fs -test -d user/data/processed || hadoop fs -mkdir user/data/processed

# Copy the Kaggle dataset to HDFS from the given path
hadoop fs -test -e user/data/tweets.csv || hadoop fs -put "$file_path" user/data/tweets.csv