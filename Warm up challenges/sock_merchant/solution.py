import math
import os
import random
import re
import sys
from collections import Counter
    
input()
socks= Counter(map(int,input().strip().split()))
pairs=0
for s in socks: 
    pairs += int(socks[s]/2)
print(pairs)
