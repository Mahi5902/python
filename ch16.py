# ERROR vs EXCEPTIONS
# Errors(unfixable)
# syntax error -wrong Syntax
# IndentationError-bad spacing
# Exceptions(handlable)
# zeroDivisionError
# TypeError
# ValueError
# FileNotFoundError

# try : wrap the riskey code
# except: handle the exception
# else : runs only when no exception occurs
# finally: always runs-- good for cleanup
# raise manually throw your own exception 

# num=int("hello")  #value error
a=int(input("pleasse tell your 1st number: "))
b=int(input("pleasse tell your 2nd  number: "))
try:
 print(a/b)
except Exception as err:
 print(f"sorry an error occured as {err}")
 name=input("tell your name: ")
else:
 print("No error occurs") 
finally:
 print("there is no error or there is no error I will run") 