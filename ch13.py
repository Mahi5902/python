
                     # TUPLE
# tuple is immutable list (you cant c hange it)

a=["monday","tuesday",123,567,123,123,123]
tup=tuple(a)
print(tup)

# tuple methods (only 2)
print(tup.index("tuesday")) #index of string tuesday
print(tup.count(123))     #count the freq of 123 in tuple


# example wehe we use tuple
def students():
     return "mahi",26,"yadav@gmail.com"
info=students()
name,age,mail=info
print(name)
