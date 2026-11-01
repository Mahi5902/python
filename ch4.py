# string and type conversion
# unicode :every character have unicode can seen using ord(val)
a="H"
print(ord(a)) #ord() gives unicode


a="college"
#indexing positive (0,1,2,3,....n-1)
print(a[0])
# indexing negative (-1,-2,-3,-4.......-n)
print(a[-1],a[6])
# slicing A[start,stop,steps]
print(a[3:6:1]) #a[start:stop:step] leg
print(a[0:7:2])





#TASK  
b="HELLO HOW ARE YOU"
print(b[6:9])
print(b[14:17])
print(b[0:5])


# TYPE CONVERSION

# you can convert a value from one type to another using these built-in function
# int(), float(), str(), bool() 
# implicit(Autoatic) -->python converts automatically when needed
#  explicite(Manual) --> tell python to convert
a="12"
b=30
print(type(a))
a=int(a)
print(type(a))

# explicit 
a=12
a=str(12) #int to string
print(a)

# implicit
b=12
print(b/12) #int to float
