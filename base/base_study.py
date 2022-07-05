
## 콘솔 출력 print 함수
print("Hello World! ", end="")
print("Hello World! ")


## 변수 선언 & 자료형 (Value Type) 
int_1 = 1   # 정수
print(type(int_1), " : ", int_1)

float_2 = 2.2   # 실수
print(type(float_2), " : ", float_2)

string_3 = "three"   # 문자열
print(type(string_3), " : ", string_3)

list_4 = ["a","b","c"]   # 리스트
print(type(list_4), " : ", list_4)

tuple_5 = ("d", "e", "f")   # 튜플
print(type(tuple_5), " : ", tuple_5)

dict_6 = {"A":"에이","B":"비","C":"씨",}  # 딕셔너리
print(type(dict_6), " : ", dict_6)


## 연산자
print(10+10) # 더하기
print(20-10) # 빼기
print(3*10) # 곱하기
print(2**10) # ** : 제곱 
print(40/10) # 나눗셈 (float 타입으로 출력)
print(55//10) # 나눗셈의 몪(나누는 대상 타입으로)
print(66%10) # 나눗셈의 나머지(나누는 대상 타입으로)

## 반올림
print(round(3.4444))
print(round(3.4444,1))

## math 외부모듈 : 올림
print(math.ceil(-3.44)) # <int>
print(math.ceil(3.44)) # <int>

## math 외부모듈을 사용한 내림 
import math 
print(math.trunc(3.44))
print(math.floor(3.44))

## # 내부모듈 int 형변환은 trunc 내림과 동일한 효과를 낸다
print(int(-3.14))