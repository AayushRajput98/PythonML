def avg(marks):
    assert len(marks)!=0, "No marks entered"   #Raise an error when the condition is matched
    return sum(marks)/len(marks)
marks=[20,18,13,18,19]
marks1=[]
print(avg(marks))
print(avg(marks1))