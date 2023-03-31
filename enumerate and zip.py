
list1 = ['A', 'B', 'C']
list2 = [1, 2, 3]

# enumerate
for x, y in enumerate(list1, start=10):
    print(x, y)


# zip
for m in zip(list1, list2):
    print(f'{m[0]}==>{m[1]}')
