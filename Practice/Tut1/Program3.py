def power(base,exp):
    power=1
    for i in range (1,exp+1):
        power=power*base
    return power
base=int(input("Enter the base"))
exp=int(input("Enter the exponent"))
print(power(base,exp))