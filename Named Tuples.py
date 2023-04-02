import collections

Person = collections.namedtuple("Pers", "Name Gender Year")

Mike = Person("Mike", 'M', 1968)
Irsa = Person("Irsa", 'F', 1970)


print(Mike)
print(Irsa)


print(Mike.Year)
print(Irsa.Gender)
# Replace

John = Person("John", 'M', 1990)

John = John._replace(Year=1985)

print(John)
