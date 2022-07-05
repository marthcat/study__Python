
### 주석
- 주석 : 코드로 들어가지 않는 텍스트 입력
  ```python
  # 주석. 음 주석
  ```

### 외부 모듈 참조
- import
  ```python
  # import ex
  import keyword
  print(keyword.kwlist)
  ```
----

### 콘솔 텍스트 출력
- print(...) : 개행하지 않는 콘솔 텍스트 출력
  
  ```python
  print("Hello! Python Programming...")
  # print("Hello! Python Programming...", END='\n') # '\n' 개행을 의미하는 특수기호
  print("String", end='') # 개행 없음
  ```

## 변수 선언 & 주로 쓰는 자료형 (Value Type) 
- 숫자형
  ```python
  int_1 = 1   # 정수
  print(type(int_1), " : ", int_1)

  float_2 = 2.2   # 실수
  print(type(float_2), " : ", float_2)

  # 외, 복소수형 등...
  ```
- 문자형
  ```python
  string_3 = "three"   # 문자열
  print(type(string_3), " : ", string_3)
  ```
- 열거형
  ```python
  list_4 = ["a","b","c"]   # 리스트
  print(type(list_4), " : ", list_4)

  tuple_5 = ("d", "e", "f")   # 튜플
  print(type(tuple_5), " : ", tuple_5)

  dict_6 = {"A":"에이","B":"비","C":"씨",}  # 딕셔너리
  print(type(dict_6), " : ", dict_6)
  ```
  
