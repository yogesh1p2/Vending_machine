class Item:

    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def display(self):
        print(self.name,"\t",self.price,"\t",self.stock)

class Cust:
    m = 0

    def give_money(self):
        Cust.m = int(input("Enter money"))

    def add_money(self):
        Cust.m = Cust.m + int(input("Enter money"))

    def return_money(self):
        print("Returning {}rs".format(Cust.m))
        print("Welcome again")
        Cust.m = 0
    
def ask_buy_fill():
    in_=input("do you want to buy or fill item \n b=buy \n a=add item \n")
    if in_ == 'b':
        ask_money()
    elif in_ == 'a':
        pass

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

def display_item(n):
    print("no.\tname\tprice\tstock")
    for j in range(n):
        print(j+1,"\t",end="")
        li[j].display()
    

def ask_money():
    global c1
    c1.give_money()
    ask_item()

def check_money(no):
    print(c1.m,"###",li[no].price)
    if c1.m>li[no].price:
        give_item(no)
        
def ask_item():
    no = int(input("Enter item number : "))
    check_money(no-1)
        
def give_item(no):
    global n
    if li[no].stock == 0:
        print("Item not available")
        continue_or_not()
    else:
        li[no].stock -= 1
        c1.m = c1.m - li[no].price
        print("Take your item {} and {}rs is pending".format(li[no].name,c1.m))
        if c1.m == 0:
            display_item(n)
        else:
            continue_or_not()            

def  continue_or_not():
    global n
    in_=input("do you want to buy other item : [y/n]")
    if in_ == 'y':
        ask_item()
    else:
        c1.return_money()
        display_item(n)
        ask_buy_fill()

while True:
    li = []
    print("Removed all available item now refill again")
    n = get_integer("number","Items") # n = number_of_item
    for i in range(n):
        name = check_for_availability(li,i+1)    
        price = get_integer("price",name)
        stock = get_integer("stock",name)
        li.append(Item(name,price,stock))
    c1 = Cust()
    display_item(n)
    ask_buy_fill()
    
    
    
    
    


        
