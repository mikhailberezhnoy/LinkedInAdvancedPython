def fil_func1(x):
    if x % 2 == 0:
        return False
    return True


def fil_func2(x):
    if x.isupper():
        return False
    return True


def square_func(x):
    return x**2


def map_func(x):
    if x < 10:
        return 'Bad'
    elif x < 20:
        return 'So-so'
    else:
        return 'Ok'


# filter only odd numbers

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = list(filter(fil_func1, list1))
print(list2)

# filter only lower case
s1 = "aSjkjsSldfkfIOIOszx"
s2 = "".join(filter(fil_func2, s1))
list3 = list(s2)
print(s2)
print(list3)

# map
list4 = list(map(square_func, list1))
print(list4)

#
s1 = (1, 12, 50, 100, 3)

list5 = list(map(map_func, s1))
print(s1)
print(list5)
