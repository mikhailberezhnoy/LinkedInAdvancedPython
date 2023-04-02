import collections

from collections import Counter

list1 = [1,2,3,4,2,3,'A','b']


cc = Counter(list1)

print (cc.values())
print (cc.items())
print (cc.most_common())


s1 = 'Ababagalamaga'

cc2 =  Counter(s1)

print (cc2.values())
print (cc2.items())
print (cc2.most_common(2))

# add s2 to counter
s2 = 'Malaga'
cc2.update(s2)

print(cc2)

# add s2 to counter

cc2.subtract(s2)

print(cc2)

print(cc&cc2)