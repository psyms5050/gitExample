# 문자열 인덱싱(Indexing)
#s = "Hello"
#print(s[0])

#문자열 슬라이싱(Slicing)

# s = "Apple"
# print(s[1:3]) # pp 1이상 3미만
# print(s[0:4]) # Appl
# print(s[2:])  # ple

#문자열의 연산 (합치기,반복)
# a = "Hello"
# b = "World"
# c = a + b
# print(c)
# print(a * 3)

# #"와 ' 같이 사용하기
# a = "모두 '안녕'이라 인사해요"
# a = '모두 "안녕"이라 인사해요'
# print(a)

#find 함수
# a = "Hello"
# print(a.find("ll")) #해당 검색 문자열이 시작하는 위치를 반환

# #len 함수
# print(len(a))

# a = "Good Morning"
# a = a.replace("Morning","Afternoon")
# print(a)

# 문자열 나누기 - split

# a = "Good Morning"
# li = a.split() # 기본값은 공백을 기준으로 나눈다.
# print(li)

# 문자열 나누기 - partition
# a = "Good Morning"
#
# left,mid,right = a.partition(" ")
# print(left)
# print(right)

# a = "Hello World"
# print(a.upper())
# print(a.lower())
#
# 공백 지우기

# a = "   Hello    "
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
