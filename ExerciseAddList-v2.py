"""
Implement the function addList()
It's purpose is to add the elements of 2 lists by pair
Ex:
l1=[5,6,7]
l2=[2,3,1,6,8]
l3=addList(l1,l2)
print(l3) # [7,9,8,6,8]
"""
def addList(list1, list2, default=0):
    result=[]
    if len(list1) > len(list2):
        for ix in range(len(list2)): # range(2) -> 0 1
            # this loop concerns the index of the
            # elements that exist in both list
            result.append(list1[ix]+list2[ix])
            
        for ix in range(len(list2), len(list1)): # range(2, 5) -> 2 3 4
            # this loop concerns the index of the
            # elements that exist only in list1
            result.append(list1[ix]+default)
    else:
        for ix in range(len(list1)):
            # this loop concerns the index of the
            # elements that exist in both list
            result.append(list1[ix]+list2[ix])
        for ix in range(len(list1), len(list2)):
            # this loop concerns the index of the
            # elements that exist only in list2
            result.append(list2[ix]+default)
    return result

l1=[5,6,7]
l2=[2,3,1]
l3=addList(l1,l2)
print(l3) # [7,9,8]

l1=[5,6,7]
l2=[2,3,1,6,8]
l3=addList(l1,l2)
print(l3) # [7,9,8,6,8]

import timeit
print("Timeit: ", timeit.timeit('addList(l1,l2)', globals=globals()))

l1=[5,6,7]
l2=[2,3,1,6,8]
l3=addList(l1,l2,10)
print(l3) # [7,9,8,16,18]

