"""
A list is an iterable object (for loop + sum(), min(), max(), map(), ...)
A list is mutable
A list is a sequence 

"""

l1=[56,67,78]
print(l1, type(l1))

l1=list() # Empty list
print(l1, type(l1))
l1=list("abcdef") 
print(l1, type(l1))

for e in l1:
    print(e)
    
for res in enumerate(l1):
    print(res[0], res[1])

for ix,e in enumerate(l1):
    print(ix, e)
    
ix=0
while ix < len(l1):
    print(l1[ix])
    ix+=1
    
l1.append(23) # a method 
print(l1)





