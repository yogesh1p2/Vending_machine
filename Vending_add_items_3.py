class Item:

    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def display(self):
        print(self.name,"\t",self.price,"\t",self.stock)

def check_for_availability(li,j): # variable j is a representation of i+1 in this function(keeping j+1 will add 1 more to our data passed of(j+1)) 
    name = input("Enter name of item {}: ".format(j))
    if len(li)==0:
        return name
    else:
        for q in range(len(li)):
            if name == li[q].name:
                name = get_correct_option(li,j,name)
                break
        return name
        

def get_correct_option(li,j,name):
    k = input("Item exists do you want to add this item [yes/no]:")
    if k.lower()=='y' or k.lower()=='yes':
        return name
    elif k.lower()=='n' or k.lower()=='no':
        return check_for_availability(li,j)
    else:
        print("Enter correct option as mentioned")
        return get_correct_option(li,j,name)
            

    
            
def get_integer(x,name):
    y = True
    while y:
        try:
            a = int(input("Enter {} of {} : ".format(x,name)))
            if a>=0:
                y = False
                return a
            else:
                print("Value should be a whole number")
        except:
            print("Enter a whole number")
            

li = [] # items
n = get_integer("number","Items") # n = number_of_item


for i in range(n):
    name = check_for_availability(li,i+1)    
    price = get_integer("price",name)
    stock = get_integer("stock",name)
    li.append(Item(name,price,stock))

print("no.\tname\tprice\tstock")
for j in range(n):
    print(j+1,"\t",end="")
    li[j].display()
