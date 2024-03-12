#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path=$1
default_dir=/user/datascience

# # Check if the file path provided exists
if [ ! -f "$file_path" ]; then
    echo "Error: File '$file_path' does not exist."
    exit 1
fi

# This script is used to initialize the HDFS file system
hadoop fs -test -d $default_dir/data || hadoop fs -mkdir $default_dir/data
hadoop fs -test -d $default_dir/data/kaggle || hadoop fs -mkdir $default_dir/data/kaggle
hadoop fs -test -d $default_dir/data/processed || hadoop fs -mkdir $default_dir/data/processed

# Copy the Kaggle dataset to HDFS from the given path
hadoop fs -test -e $default_dir/data/kaggle/tweets.csv || hadoop fs -put "$file_path" $default_dir/data/kaggle