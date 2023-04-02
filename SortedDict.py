import collections
from collections import OrderedDict
# Items with L,W,H
d1 = [  ("Item1",(10,14,8)),
        ("Item2",(11,4,18)),
        ("Item3",(1,6,17))
        ]

sortedbyL = sorted(d1, key = lambda x: x[1][0], reverse=False)
sortedbyW = sorted(d1, key = lambda x: x[1][1], reverse=False)
sortedbyH = sorted(d1, key = lambda x: x[1][2], reverse=False)
print (sortedbyL)
print (sortedbyW)
print (sortedbyH)

#--------------
ODict = OrderedDict(sortedbyL)
print (ODict)

item, size = ODict.popitem(False)
print(item,size)

for i,j in enumerate(ODict, start =1):
        print (i, j)

# Comparison

a = OrderedDict({'x':1, 'y':2, 'z':3})
b = OrderedDict({'x':1, 'y':2, 'z':3})
print ('Check1:', a==b)  #True


a = OrderedDict({'x':1, 'z':3, 'y':2})
b = OrderedDict({'x':1, 'y':2, 'z':3})
print ('Check1:', a==b)  # False because if different order



a = {'x':1, 'z':3, 'y':2}
b = {'x':1, 'y':2, 'z':3}
print ('Check1:', a==b) # True



a = OrderedDict({'x':1, 'z':3, 'y':2})
b = {'x':1, 'y':2, 'z':3}
print ('Check1:', a==b) # True