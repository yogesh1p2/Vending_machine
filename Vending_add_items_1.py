class Item:

    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def display(self):
        print(self.name,"\t",self.price,"\t",self.stock)

i = [] # items
b=True
n = int(input("Enter number of item : ")) # n = number_of_item

for j in range(n):
    name = input("Enter name of item {}: ".format(j+1))
    price = input("Enter price of {} : ".format(name))
    stock = input("Enter stock of {} : ".format(name))
    i.append(Item(name,price,stock))

print("no.\tname\tprice\tstock")
for j in range(n):
    print(j+1,"\t",end="")
    i[j].display()
