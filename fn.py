#arguments fn and parameter fn

def myAge(age):
    print("my age is", age)

myAge(34) 

#find the area of square using function

area= int(input("enter the square side"))
def areaS(side):
    return side*side
output = areaS(area)
print("area is",output)    

#DELIVERY COST; FOOD COST; PRICE; DISCOUNT; VAT. FIND THE PRICE.

#delivery cost , food cost , price, discount , vat 
cost= int(input("enter the price of food"))
delivery= int(input("enter the delivery price of food"))
discount= int(input("enter the discount given on food"))
vat= int(input("enter the vat given on food"))
def price(cost,delivery,discount,vat):
    return cost+delivery-discount+vat
price=price(cost,delivery,discount,vat)
print("price of food is",price)
