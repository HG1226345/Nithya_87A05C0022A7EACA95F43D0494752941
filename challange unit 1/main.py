number= int(input("please enter any number to find factorial:"))
fact=1
for i in range(1,number + 1):
     fact = fact * i
print("the factorail of %d is =%d" %(number,fact))