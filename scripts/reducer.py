#!/usr/bin/python3
"""reducer.py"""

import sys
from collections import Counter

previous = None
sum = 0
word_count = Counter()

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    key, count = line.split('\t', 1)

    # if the current word is different from the previous word
    # print the word and its frequency provided the previous word is not None
    if key != previous:
        if previous is not None:
            print(f'{previous}\t{sum}')
        previous = key
        sum = 0
         
    # increase the frequency of the current word
    sum += int(count)

if previous is not None:
    print(f'{previous}\t{count}')