mylist = (1, 2, 3)

x = iter(mylist)

print(next(x))
print(next(x))
print(next(x))

for x in mylist:
    print(x)