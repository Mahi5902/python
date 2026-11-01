# 1)print all positive and negative element seperately input[3,-1,,4,-5,9]
#2) find the mean(average) of all list elements [10,20,30,40]
# 3)find the greatest element and print its index [4,8,2,9,1]
#4) find the second greatest element    [4,8,2,9,1]
#5)check if the list is already sorted   [1,3,5,7]


# (1)
a= [3,-1,4,-5,9]
pos=[]
neg=[]
for i in range(0,len(a)):
     if(a[i]>=0):
          pos.append(a[i])
     else:
          neg.append(a[i])  
print("positive elements are:")             
print(pos)
print("Negative elements are: ")
print(neg)

# (2)
b=[10,20,30,40]
count=0
sum=0
for i in b:
     sum+=i
     
print(f"your average is: {sum/len(b)}")     

#(3)
c=[4,8,2,9,1]
maxi=c[0]
index=0
for i in range(1,len(c)):
     if(c[i]>maxi):
        maxi=c[i]
        index=i  
print(f"maximum value is :{maxi}")
print(f"maximum element is at : {index}")


#(4)
d=[4,8,2,9,1]
maxi1=d[0]
maxi2=d[0] 
for i in range(3,len(d)):
     if(maxi1<d[i]):
      maxi2=maxi1
      maxi1=d[i]    
     elif(d[i]>maxi2) :
         maxi2=d[i]
print(f"second largest element is : {maxi2}")


#(5)
e=[1,3,5,7]
flag=0
for i in range(1,len(e)):
    if(e[i-1]>e[i]):
        flag=1
        break
if(flag==1) :print(f"{e} list is not sorted")
else: print(f"{e} list is  sorted")
