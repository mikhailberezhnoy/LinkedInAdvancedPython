import collections
from collections import  deque

dq = deque('abcdef')

dq.pop()
print (dq)


dq.popleft()
print (dq)


dq.append('x')
print (dq)


dq.appendleft('y')
print (dq)

# Rotate
d2=deque('ABC')
d2.rotate(1)
print(d2) #deque(['C', 'A', 'B'])
d2.rotate(1)
print(d2) #deque(['B', 'C', 'A'])