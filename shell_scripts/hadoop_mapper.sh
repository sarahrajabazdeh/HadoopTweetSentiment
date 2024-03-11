#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <hadoop_path>"
    exit 1
fi

hadoop_tools = "/usr/local/hadoop/share/hadoop/tools"

hadoop jar $hadoop_tools/lib/hadoop-streaming-2.7.3.jar \
    -file ../scripts/mapper.py \
    -mapper mapper.py \
    -file ../scripts/reducer.py \
    -reducer reducer.py \
    -input user/data/processed/tweets_subset \
    -output user/data/dict