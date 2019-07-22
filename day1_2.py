#(변수명) = (초기화 값)
#inputVal = input("문자열을 입력하세요: ")
#print("입력된 문자열은 : ",inputVal ,"입니다.")
#print("inputVal의 자료형은 ",type(inputVal))

# inputVal = input("첫번째 정수를 입력해주세요 : ")
# inputVal2 = input("두번째 정수를 입력해주세요 : ")
# print("입력된 정수는",inputVal,"입니다")
# print("inputVal의 자료형은",type(inputVal))
#
# if (inputVal.isdigit() == True) and (inputVal2.isdigit() == True):
#     inputVal,inputVal2 = int(inputVal),int(inputVal2)
#     print(inputVal + inputVal2)
#     print(inputVal - inputVal2)
#     print(inputVal * inputVal2)
#     if not(inputVal2 == 0) == True:
#         print(inputVal / inputVal2)
#         print(inputVal % inputVal2)
#         print(inputVal // inputVal2)
#         print(inputVal ** inputVal2)
#     else:
#         print(0)
#         print(0)
#         print(0)
# print(type(inputVal))

#실습 1. 원의 부피 구하기

# inputVal = input("구의 반지름을 입력하세요 : ")
# if(inputVal.isdigit() == True):
#     inputVal = int(inputVal)
#     s = 4 / 3 * (inputVal ** 3 * 3.14)
#     print(s)
#     print(round(s))
#
# 실생활 사용 -> 10진수 0과 1로만 이뤄진 수 -> 2진수
# print(bin(10))
# binNum = bin(10)
# hexNum = hex(10)
# print(int(binNum,2))
# print(int(hexNum,16))
#
#
# 비트 연산자
# n,m = 2, 7
# print(bin(n), "^", bin(m) , " = " , n ^ m)  #xor 연산
# print(bin(n), "|", bin(m) , " = " , n | m)  #or 연산
# print(bin(n), "&", bin(m) , " = " , n & m)  #and 연산
#
# n, m = 5,2
#
# print(n <= m)           #false
# print(n >= m)           #true
# print(n < m)            #false
# print(n > m)            #true
# print(n == m)           #false
# print(not(n == m))      #true

# 할당 연산자
# a = 5
# b = 3
#
# a **= b
#
# print(a)

# 식별 연산자

# a = 5
# b = 5
#
# print(a is b)
# print(a is not b)

# 멤버 연산자
# print("Hello" in "Hello World")
# print("Hello" not in "Hello World")