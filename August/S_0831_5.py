import random

myList = [1,2,3,4,5,6]

while(True) :
    response = input("주사위 계속 던질거야? yes / no : ");
    if response == "yes" :
        coin = random.choice(myList)
        print(coin)
    else:
        break