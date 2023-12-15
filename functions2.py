import random

accounts = {"78767876":{"name":"helen","balance":300,"age":12}, "4567876545":{"name":"helen","balance":0.00}}
def add():
    a = 2
    b = 3
    result = a+b
    print(result)
    

print(add())


def account_generation():
    accnum = "89"
    for i in range(1,8):
        accnum+= str(random.randint(1,9))
        
    for i in range(len(accounts)):
        if(i == accnum):
            account_generation()
        else:
            print("hi")


account_generation()
print(accounts)
accounts["78767876"]["balance"] += 500000
print(accounts["78767876"]["balance"])
        
        