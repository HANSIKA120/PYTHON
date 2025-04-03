'''a= int(input("enter no."))
for i in range(1,a+1):
        print("*" *i)
        
       
       
#q8   [*]pattern        
a= int(input("enter no."))
 
for i in range(1,a+1):
        print(" "*(a-i),end="")
        print("*"*(2*i-1)) 
 '''       
        
#q9   ***
#     * *
#     ***
a=int(input("print a number"))
for i in range(1,a+1):
        if (i==1 or i-a==0):
           print("* "*3)    
        else:
           print("*"," ","*")            


        
        
'''
for i in range (1,4):
        print("*" *(4-i))
        
        
a=1    
b=2    
for i in range (1,4):
        print(" "*b, "*" *a)
        a+=2
        b-=1




a=int(input("enter a number: "))
for i in range(1,11):
    print(a,"X",11-i,"=",a*(11-i))
    





a = int(input('enter the number:'))

i=1
s=1

# f= n!
while(i<=a):
        s*=i
        i+=1
  
print(s)  

'''
# t= (4, 6, 7, 8, 9, 89, 45)
# for i in t[1:7]:
#     print(i)
'''    
    
l=["harry","soham","sakshi","ron"]




#prime no.
a=(int(input("enter no. :  ")))

if all(a%x != 0 for x in range(2,a)):
        print("it is a prime numbert!")
else:
        print("not")    

'''
        
        
            

    
a = int(input('enter the number:'))
#for x in range(1,11):
i=1
while(i<11):
        print(a,"X",i,"=",a*i)
        i+=1
        
        
        
        
        
a = int(input('enter the number:'))

i=1
s=0
#sum= n/2* (a+(a+(n-1)*d))
while(i<=a):
        s+=i
        i+=1
  
print(s)     



   



