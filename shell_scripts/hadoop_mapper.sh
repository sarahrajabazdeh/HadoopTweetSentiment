#!/bin/bash
hadoop_tools="/usr/local/hadoop/share/hadoop/tools"
local_base_dir="/home/datascience"
hadoop_base_dir="/user/datascience"

hadoop jar $hadoop_tools/lib/hadoop-streaming-2.10.0.jar \
    -file $local_base_dir/scripts/utils.py \
    -file $local_base_dir/scripts/mapper.py \
    -mapper mapper.py \
    -file $local_base_dir/scripts/reducer.py \
    -reducer reducer.py \
    -input $hadoop_base_dir/data/processed/tweets_subset \
    -output $hadoop_base_dir/data/dict