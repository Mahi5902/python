#conditional statement

if 12==12:
     print("hello how are you !")
#task
num1=int(input("Enter the num1 of Person1: "))
num2=int(input("Enter the num2 of Person2 :"))
    #if-elif-else 
if num1>num2:
 print(f"{num1} is greater than {num2}")
elif num2>num1:
 print(f"{num2} is greater than  {num1}")
else:
  print(f"{num1} and { num2} both are equal.")
  
#if-elif
rupees=int(input("Enter your total amount:"))
if rupees==10:
  print("I will have a chocobar")
elif rupees==50:
  print("I will have manchurian")
elif rupees==100:
 print("mcd")
elif rupees==500:
 print("5 star dhaba") 


#check even or odd
a=int(input("enter any number :")) 
if a%2==0:
  print(f"number {a} is even.")  
else:
  print(f"number {a} is odd .")

  #check it is leap year or not
year=int(input("enter any year:"))
if year%100==0 and year%400==0:
    print(f"year {year} is leap year")
elif year%100!=0 and year%4==0:
  print("leap year")
else:
  print("not a leap year")  
