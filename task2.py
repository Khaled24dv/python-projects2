
### task 2 :
### instant discount system :
print("wellcome")
price = int (input("enter your price :"))
if price <100:
    print(f"The Val Discount Is (%0) and price = {price}")
elif price > 100 and price < 500:
    
    print(f"The Val Discount is 10% and price = {price-price*10/100}")
    print(f"the val discount is {price*10/100}")
elif price>=500:
  
    print(f"The Val Discount Is 20% And The price = {price-price*20/100}")
    print(f"the val discount is {price*20/100}")
else: 
    print("Not Information Avilable")
