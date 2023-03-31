
#iter() & next()

list1 = [1, 2, 4, 'A']

#Var1
i = iter(list1)

while x := next(i, 1j):
    if x == 1j:
        print('Stopping...')
        break
    print(x)

#Var2
for x in iter(list1):
    print (x)