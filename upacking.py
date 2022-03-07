

l1=[56,78,89,100,200]

# a,b,c,d=l1  # unpacking is used

# print(a,d)

a,*other,d=l1  # unpacking is used

print(a,d, other)