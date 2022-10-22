count = 10
while count > 0:
    money = int(input("돈을 넣어주세요:"))
    if money == 300:
        print("커피를 줍니다.")
        count -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        count -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % count)

print("커피 판매 완료^_^)b")
