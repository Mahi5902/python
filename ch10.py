def multiply(a,b,c,d):
     print(a*b*c*d)
multiply(1,2,3,4)

#defaults arguments
# if you are writing c=12 then write these thing in parameter at end 
def addition(a,b,c=12):
     print(a+b+c)
addition(5,5,5)  

# keyword arguments
def subtraction(a,b):
     print(b-a)
subtraction(50,b=30)     