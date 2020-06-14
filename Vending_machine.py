import time
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

    def deduct_money(self,p):
        Cust.m = Cust.m - p
        return Cust.m

    def return_money(self):
        print("Returning {}rs".format(Cust.m))
        print("Welcome again")
        Cust.m = 0

class Machine:
    tries_attemp = 1

    def increase(self):
        tries_attemp+=1
        

def add_item():
    id_num="1234"
    while p1.tries_attemp<=3:
        id_check = input("enter the password(it is 1234) : ")
        if id_check==id_num:
            print("Hello, refill items and collect money")
            p1.tries_attemp = 1
            break
            
        elif p1.tries_attemp == 3:
            print("you have failed 3 times.\n System is locked")
            print("Event has been registered")
            print("Please send email to reset password")
            break

        elif id_check != id_num:
            print("incorrect entry no :",p1.tries_attemp)
            print("system will be locked with three incorrect entry")
            print("Event has been registered")
            p1.tries_attemp+=1    
            
def y_n(i):
    x = True    
    while x:
        if i == 'y':
            x = False
            return True
        elif i == 'n':
            x = False
            return False
        else:
            print("enter y for yes or n for no")


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


def  continue_or_not():
    print("Money pending is {}rs".format(c1.m))
    in_=input("do you want to buy other item : [y/n]")
    if in_ == 'y':
        ask_item()
    else:
        c1.return_money()
        display_item()
        ask_buy_fill()   
        
def give_item(no):
    global n
    if li[no].stock == 0:
        print("Item not available")
        continue_or_not()
    else:
        li[no].stock -= 1
        c1.deduct_money(li[no].price)
        print(c1.m)
        print("Take your item {}".format(li[no].name))
        if c1.m == 0:
            display_item()
            print("Thank you visit again")
            ask_buy_fill()
        else:
            continue_or_not()            

def check_money(no):
    if c1.m>=li[no].price:
        give_item(no)
    else:
        print("Cost of item is {}".format(li[no].price))
        continue_or_not()

def ask_item():
    no = int(input("Enter item number : "))
    check_money(no-1)

def ask_money():
    c1.give_money()
    ask_item()

def ask_buy_fill():
    in_=input("do you want to buy or fill item \n b=buy \n a=add item \n")
    if in_ == 'b':
        ask_money()
    elif in_ == 'a':
        if p1.tries_attemp < 3:
            add_item()
            ask_buy_fill()
        else:
            print("System is locked")
            print("Please send email to reset password")
            ask_buy_fill()
            
def display_item():
    global n
    print("no.\tname\tprice\tstock")
    for j in range(n):
        print(j+1,"\t",end="")
        li[j].display()

p1 = Machine()

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
    display_item()
    ask_buy_fill()
    
    
    
    
    
    


        
