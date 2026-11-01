# #ranges--generate a sequence of numbers. think of it as saying"count from here to there"
# # range(stop) 0 to stop-1
# # range(start,stop) start to stop-1
# # range(start,stop,step) start up to stop-1 jumping by step
# #10-100
# #23-56
# #0-45
# # range(10,101,1)
# # range(23,57,1)
# #range(46)

# for i in range(10,21,1):
#      print(i)
# for i in range(23,57,1):
#      print(i)
# for i in range(46):
#      print(i)  

# #table of 5
# for i in range(5,51,5):
#      print(i)
#   #TASK  
# #   loop at valiables 
# #print table of any number entered by user
# num=int(input("Enter number: "))
# for i in range(num,(num*10)+1,num):
#      print(i)

# # loop for string 
# a="students"
# for i in a:
#      print(i)
# for i in range(len(a)):
#      print(f"{i}:{a[i]}")


     # break,continue & else
# else work with break
for i in range(1,11):
 if(i==45):
    break
 print(i)
else:
 print("no break was encountered")

for i in range(1,5):
  if(i==2):
    continue
  print(i)