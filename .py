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

x=0
while True:
    y= int(input("guess number"))
    if y ==x:
         print ("you guess correctly")
         break
    if x>y:
         print ("less than correct guess")
         if y>x:
              print ("greater than correct guess")
