# while loop
#1)print digits of a number in new line
#2)accept number and print reverse
#3)check number is palindrome
#4)build a number guessing game-computer picks a random number,user keeps guessing until correct
a=int(input("enetr any number :"))
while(a):
     r=a%10
     a=a//10
     print(r)


# reverse a number
ans=0
b=int(input("Enetr any number :"))
x=b
while(b):
     r=b%10
     ans=ans*10+r
     b=b//10
print(ans)     
if(ans==x):
     print("number is palindrome")
else:
     print("Number is not a palindrome")     