# the 4 inbuilt datastructure
               #     ordered   mutable   duplicates  accessed by
# list               yes        yes         yes       index
# tuple              yes        no          yes       index
# set                no        yes          no        methods
# dictionary         yes       yes        keys:no     key

# (linkedlist,queue,tree,hashmap)

# 1)LIST

# list have mutable nature
a=[12,12,24,36,45]
print(type(a))
print(a[4])

# traversing on values
for i in a:
 print(i)

#  traversing on index
for i in range(0,len(a)):
 print(a[i])

#  Method of list
# CRUD-> Create,read, update,delete
print("methods operations")
a.append(12)  #append at end
a.insert(0,5)  #a.insert(index,value)
a.remove(12)   # remove 1 remove(x) x should be in list
a.pop()       #Remove and return item at index (default last).
a.sort()     #sort in ascending and return None
a.sort(reverse=True)  #sort in descending order
a.reverse()  #reverse in place
print(len(a))         #number of items

print(a)
# string is immutable in nature
b="KHGN"
