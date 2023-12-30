class customer:
    def__init__(self , name , balance= 0 ):
    self.name = name
    self.balance = balance 
    print(" the __init__method was called ")

cust = customer (" lara " , 100)
print(cust.name) 
print(cust.balance) 
