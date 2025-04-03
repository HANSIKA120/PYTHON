#error handeling

# try:
#     TabError
# catch:
#     type of error


try:
   print(x)   #name error
except NameError:
   print("x net defined ")

# y=1/0         #zerodivision error
#print(y)
try:
    y=1/0
    print(y)
except ZeroDivisionError:
   print(" zerodivision error")


# a="hansika"  #problem error
# #b=int(a)     #value error
# print(b)   
# try:
#     a="hansika"
#     b=int(a)
# except ValueError:
#      print(" string not const in int error")






mylist=["pawan","ron","ivan"]
# print(mylist[4])      #indexerror
try:
     print(mylist[4])
except IndexError:
     print("index error")




import os
try:
 os.remove("myfile.txt")  #FileNotFoundError
except FileNotFoundError:
   print("file not found")





x="pawan"
y=4
try:
    c=x+y
except TypeError:
    print("interoot range")



x="hansi"
y=4
#c= x+y 
#print(c)  
try: 
   c=x+y
   print(c)  
except TypeError:
   print("type error")

finally:
    print("always run")   