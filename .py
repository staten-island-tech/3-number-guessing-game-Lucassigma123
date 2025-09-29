# import random
# randomint=random.randint(1,10)
# print(randomint)

import random
integer= random.randint(1,10)
while True:
    guess= int(input("guess the number 1-10"))
    if guess== integer:
        print("correct")
        print(integer)
        break
    else:print("incorrect")


