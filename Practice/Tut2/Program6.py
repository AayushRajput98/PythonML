import random
def genrate_random():
    x=random.randint(0,100)
    if x%3==0:
        return True
    else:
        return False
print(genrate_random())