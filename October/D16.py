import sys


print("인자값의 총 수는 %d개 입니다" % (len(sys.argv)-1))

for i in sys.argv[1:]:
    print(f"{i}를 입력 받았습니다")

for i in sys.argv[1:]:
    print(i, end=" ")