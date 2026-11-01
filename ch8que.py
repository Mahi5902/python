# 1) print hello world n times
#2) print natural number fron 1 to n
#3) reverse for loop print n down to 1
#4) print the multiplication table of  a number
#5)print sum till n number
#6)print factorial of n
#7) sum of even numbers and odd numbers
#8)factors of a number
#9)check if a number is perfect(sum of factors=number itself)
#10)check if a number is prime
#11)reverse string without using built-in function
#12) check if a string is palindrome
#13) count letters,digits,and special symbols in a string
n=int(input("Enter any number: "))
for i in range(n):
 print("HELLO WORLD")



print("1 to n")
for i in  range(1,n+1):
 print(i)



print("n to 1")
for i in range(n,0,-1):
   print(i)



print("multiplication table")   
for i in range(1,11):
   print(f"{n}*{i} ={n*i}")



print("summ till n")   
s=0 
for i in range(1,n+1):
  s=s+i
print(s) 



print("factorial of n")
f=1
for i in range(1,n+1):
  f=f*i
print(f)  

print("sum of odd and even numbers")
evensum=0
oddsum=0
for i in range(1,n+1):
  if(i%2==0):
    evensum+=i
  else:
    oddsum+=i
print(f"sum of odd {oddsum}")
print(f"sum of even {evensum}")

print(f"factor of number {n} :")
for i in range(1,n+1):
  if(n%i==0):
    print(i)

    
sum=0
for i in range(1,n):
  if(n%i==0):
    sum+=i
if(sum==n):
  print("number is perfect number")  
else:
  print("number is not perfect number")  


#check number is prime
count=0
for i in range(1,n+1):
    if(n%i==0):
      count+=1
if(count==2):
  print("prime number")
else:
  print("composite number")
        
#reverse string without using built-in function
a=input("Enetr a string :")
rev=""
l=len(a)
for i in range(0,l):
  rev+=a[l-1-i]
print(rev) 

#check for palindrome
false=0
for i in range(0 ,n):
  if(a[i]!=a[l-i-1]):
   false=1
   print("Not a palindrome")
   break
if(false==0):
  print("is palindrome")      

# count digits, characters,and special characters
char=0
spchar=0
digits=0
for i in a:
 if(ord(i)>=65 and ord(i)<=90 )or(ord(i)>=97 and ord(i)<=122):
   char=char+1
 elif (ord(i)>=48 and ord(i)<=57):
   digits=digits+1
 else:spchar=spchar+1
print(f"char {char}") 
print(f"digits {digits}")
print(f"special char {spchar}")
   