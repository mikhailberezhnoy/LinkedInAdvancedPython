import itertools

# cycle
list1 = [1, 3, 2, 10, 20, 0, -1]

c1 = itertools.cycle(list1)
for i in range(10):
    print (next(c1))

''''''
1
3
2
10
20
0
-1
1
3
2
''''''

# count

c2 = itertools.count(1000,20)
for i in range(10):
    print (next(c2))

''''''
1000
1020
1040
1060
1080
1100
1120
1140
1160
1180
''''''


# accumulate
c3 = itertools.accumulate(list1)
for i in range(len(list1)):
    print (next(c3))
''''''
1
4
6
16
36
36
35
''''''

# chain

list2 = [1, 3, 2, 10, 20, 0, -1]
list3 = [9,11,12]
list4 = list(itertools.chain(list2, list3))
print (list4)

# dropwhile / takewhile
print('----------DROPWHILE--------')
list5= list(itertools.dropwhile(lambda u : True if u<20 else False , list2))
print (list5)

list6= list(itertools.takewhile(lambda u : True if u<20 else False , list2))
print (list6)
