import collections

from collections import defaultdict

dd =defaultdict(lambda:100)

dd["Item1"]+=1
dd["Item2"]+=1
dd["Item2"]+=1

for x,y in dd.items():
    print (x, y)