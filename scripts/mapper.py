#!/usr/bin/env python3
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
        # Check if the word is a stopword and if it is, then skip it
        if utils.check_stopword(word): continue
        # Stem the word
        word = utils.stem(word)
        print(f'{word}\t1')  