# LIST

friendName= ["ivan","ron","nami","kanu"]
friendName.append("pawan")
friendName.append("tanya")
friendName.append("mukul")
friendName.append("manan")
for n in friendName:
    print (n)

friendName.remove("pawan")
for n in friendName:
    print (n)

print(friendName)
#for n in friendName:
#    print (n)

friendName[5]="mukul_sharma"
for n in friendName:
    print (n)



#TUPLE

mytuple=("pawan","manan","mukul","tanya")


mytupleL=list(mytuple)
mytupleL.append("any")

mytupleL.remove("any")

mytupleL[2]=("mukul_sharma")

print(mytupleL)

for n in mytupleL:
    print (n)




#SET
myset={"MANAN","TANYA","MUKUL","PAWAN"}

myset.add("HANSI")
myset.remove("MANAN")
#SET CANNOT BE MODIFIED

#DICT
mydict={ "name":"hansika",
         "age":24 }

for(value) in mydict.values():
    print(value)
mydict["name"]="manan"    
print(mydict)

mydict.update({"gender":"female"})
print(mydict)

mydict.pop("gender")
print(mydict)

