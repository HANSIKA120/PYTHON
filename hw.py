#WAP TO ADD THE 10 STUDENTS NAME IN LIST, REMOVE LAST VALUE
#REVERSE THE LIST
#SORTING THE NAME

xName=["ivan","kari","nami","ron","asha","star","rav","cye","robin","adi"]
print(xName)
xName.remove("adi")
xName.reverse()
xName.sort()

for n in xName:
    print(n)