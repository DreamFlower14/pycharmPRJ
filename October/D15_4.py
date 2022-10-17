import random

tuple = ['1', '2', '3', '4', '5', '6']

while(True):
    answer = input("주사위 던져? yes | no : ")
    if answer == "yes":
        num = random.choice(tuple)
        print(num)
    else:
        break


