import random
com=random.randint(1,100)

score=0 
tries=0
while(True):
   tries+=1
   human=int(input("guess your number between 1 and 100 :"))
   if(human==com):
     print("congrachulations! you won")
     break
     
   elif human>com:
     print("sorry! wrong guess go lower.")
   else:
     print("sorry! wrong guess go hiegher.") 


print(f"you won in tries {tries}")
