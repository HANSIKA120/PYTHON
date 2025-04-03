a=int(input("enter a number: "))
for i in range(1,11):
    print(a,"X",i,"=",a*i)
    



fruit=[]
for i in range(0,7):
    fruits=input("enter fruit:  ")
    fruit.append(fruits)
print(fruit)    






 
marks=[]

for i in range(0,6):
    mark=int(input("enter marks:  "))
    marks.append(mark)
print(marks) 

marks.sort()
print(marks)


print(sum(marks))





a=(7,0,8,0,0,9)
print(a.count(0))




dict={'chalna':'walk',
     'bhagna':'run',
     'bolna':'talk',
     'mummy':'mom',
     'bf':'headache'}

a= input("enter the key:  ")
print(dict)



x=set ()
for i in range(0,8):
    no=int(input("enter no: "))
    x.add(no)
print(x)

'''
y= set ()
y.add(45)
#y.add("56")
#y.add(67.7)

print(y)

'''


s={}

print(type(s))
s.update({'sam':'hindi'})
s.update({'ram':'hindi'})
s.update({input('name'):input('language')})
print(s)




a=int(input("enter no. 1: "))
b=int(input("enter no. 2: "))
c=int(input("enter no. 3: "))
d=int(input("enter no. 4: "))



num=[int(input("enter nos: ")) for i in range (4)]
print("max value: ", max(num))



a=input("incoming text: ")
B=a.lower()
if "make a lot of money" in B or "buy" in B or "kill" in B:
    print("SPAM!!")
else:
    print("SAFE~")


a=[int(input("marks: "))for i in range(1,4)]
b=[int(input("max marks: "))for i in range(3) ]
if(a[0]*100/b[0]>=33 and a[1]*100/b[1] >=33   and    a[2]*100/b[2] >=33 and    sum(a)*100/sum(b)  >=40 ):
    print("pass!")
else:
    print("fail")   
    
    
    