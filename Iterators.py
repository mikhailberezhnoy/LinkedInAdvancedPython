
#iter() & next()

list1 = [1, 2, 4, 'A']

i = iter(list1)

while x := next(i, 1j):
    if x == 1j:
        print('Stopping...')
        break
    print(x)
