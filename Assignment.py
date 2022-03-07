
l1=[5,6,7]
l2=l1

print(l1, id(l1))
print(l2, id(l2))

l2[0]=99
print(l1)

del l1
print(l2, id(l2))

del l2