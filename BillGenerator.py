items=[]
prices=[]
sum=0

def billgenerator(items,sum):
    print("----------")
    print("DMART SHOPPING CENTRE")
    for i in range(len(items)):
        print(f"{items[i]}\t-{prices[i]}/-")
    print("Total due amount:",sum)
    print("----------")





while(True):
    item=input("Enter item or q for quit:")
    if item.lower()=='q':
        break
    else:
        price=float(input("Enter price of the item:"))
        items.append(item)
        prices.append(price)

print("***Your Cart***")
for i in range(len(items)):
    print(f"{items[i]}-\t{prices[i]}/-")

for price in prices:
    sum=sum+price

ask=input("Do you need a bill?y or n:")
print()
if ask=='y':
    billgenerator(items,sum)
else:
    print("You have to pay:",sum)
print("Thank You,Visit Again! :)")
