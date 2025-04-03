#for loop is used to complete the iteration or repetiting the task

name= input("enter your name")

# iterate my name using for loop
# eg - in c for(int i=0; i<10;; i++)

for i in name :
    print (i)

#print no. 1 to 10

for x in range (1, 11):
    print (x)

 #print odd no.


for y in range (1,11):
    if y %2 !=0:
      print(y)

#step size

for z in range(1, 12, 2):
    print (z)


#print the even and odd nos.



for a in range(1, 21):
    if  a%2 ==0:
        print("even",a)
    else:
         print("odd ",a)    