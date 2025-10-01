# import random
# randomint=random.randint(1,10)
# print(randomint)

# import random
# integer= random.randint(1,25) #random randint is random integer
# while True:
#     guess= int(input("guess the number 1-25")) 
#     if guess== integer:
#         print("correct")
#         print(integer)
#         break
#     else:print("incorrect")
import random
history=[]
x=random.randint(1,25)
while True:
    y= int(input("guess number 1-25 "))
    history.append(y) #append adds up 
    if y ==x:
         print ("you guess correctly")
         print(history,"history")
         break
    if y < x:
         print ("less than correct guess")   
    if y > x: 
        print ("greater than correct guess")
    if y<x or y>x:
         print(history)