# 도메인 받고 비밀번호 만들어주기
# 규칙 1 : http:// 없애기
# 규칙 2 : 처음 만나는 점 (.) 포함 뒷 부분 제외
# 규칙 3 : 남은 글자 중 처음 세자리  + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
# ex) http://naver.com   ==>    nav51!

url = input("사이트를 입력하세여 : ")

# 규칙 1
password = url.replace("http://", '')  # http:// replace() 로 없애주기

# 규칙 2
jum = password.find('.')  # 처음 . 이 나오는 부분 인덱스 찾고
password = password[:jum]  # 처음부터 . 까지만 다시 password 에 넣어주기

# 규칙 3
index0 = password[:3]  # 처음 3자리
index1 = str(len(password))  # 글자 갯수
index2 = str(password.count('e'))  # 글자 내 'e' 갯수
index3 = "!"  # "!"

password = index0 + index1 + index2 + index3

print("%s의 비밀번호는 %s입니다!" % (url, password))