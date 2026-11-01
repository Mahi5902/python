# d={10:10,24:20,36:30,42:40}  
# #VANILLA PYTHON
#  # {key:value}
# print(d[24])
# # creating a new value pair 
# d[50]=300 
# # updating a key value pair
# d[10]=90
# print(d)

# method approach
d={24:20,36:30,42:40} 
q=d.fromkeys([10,20,30,40],50)
print(q)
print(d.get(24))
print(d.items())
print(d.values)
d.setdefault(30,3000)
print(d)
# merge two dictionaries into one {a:1,b:2}
# sum all values in dictionary {"a":10,"b":20,"c":30}
# count the frequency of each element in a list using a dictionary
# combine a two dicts,adding values for common keys