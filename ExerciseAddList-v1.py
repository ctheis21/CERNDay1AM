"""
Implement the function addList()
It's purpose is to add the elements of 2 lists by pair
Ex:
l1=[5,6,7]
l2=[2,3,1,6,8]
l3=addList(l1,l2)
print(l3) # [7,9,8,6,8]


l4 = [0]*4  <=> l4=[0,0,0,0]
"""

def addList(li1, li2, default=0):
    
    li1_tmp=li1.copy() # <=> li1_tmp=li1[:]
    li2_tmp=li2.copy()
    
    if len(li1) < len(li2):
        li1_tmp.extend([default]*(len(li2)-len(li1)))
        
    elif len(li2) < len(li1):
        li2_tmp.extend([default]*(len(li1)-len(li2)))   
        
    res=[]
    for i in range(len(li1_tmp)):
        res.append(li1_tmp[i]+li2_tmp[i])
   
    return res
   
    # return [li1_tmp[i]+li2_tmp[i] for i in range(len(li1_tmp))]

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

