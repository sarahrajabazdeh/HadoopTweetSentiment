#!/usr/bin/python3
"""mapper.py"""

import sys 
import utils

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    fields = line.split('\t')
    if len(fields) != 2:
        continue
   
    tweet = fields[1]
    words = utils.tokenize(tweet)
    for word in words:
        print(f'{word}\t1')  