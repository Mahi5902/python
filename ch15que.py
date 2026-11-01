# 1)merge two dictionaries into one d1={a:1},d2={b:2}==>{a:1,b:2}
# 2)sum all values in dictionary {"a":10,"b":20,"c":30} sum=60
#3) count the frequency of each element in a list using a dictionary
# ["a","b","c","b","a"] ==>{"a":3,"b":2,"c":1}
# 4)combine a two dicts,adding values for common keys
# d1={a:5,"b":3},d2={"b":4,"c":2} ==>{a:5,b:7,c:2}

#1)
d1={"a":1} 
d2={"b":2}
# d1.update(d2)
# print(d1)
for i in d2:
     d1[i]=d2[i]
print(d1)

#2) find sum
sum=0
a1={"a":10,"b":20,"c":30}
for i in a1:
     sum=sum+a1[i]
print(sum)     

#3) frequecy count
a2=["a","b","c","b","a","e","g","g","g","m","m","m"]
count=0
d={}
for i in a2:
     if(i in d.keys()):
         d[i]=d[i]+1
     else:
          d[i]=1
print(d)          

#4)# 
a3={"a":5,"b":3}
a4={"b":4,"c":2}
#  ==>{a:5,b:7,c:2}
for i in a4:
 if(i in a3.keys()):
     a3[i]=a4[i]+a3[i]
 else:
     a3[i]=a4[i]
print(a3)     
