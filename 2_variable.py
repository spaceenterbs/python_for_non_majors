# 변수의 의미와 역할 이해하기

# 추리하기 01
print(300)
print(300, 300)
print(300, 500)
print(500, 300)
print(300, 500, 300)

# 추리하기 02
a = 300
b = 500
print(a)
print(a, a)
print(a, b)
print(b, a)
print(a, b, a)

# 응용하기 01
apple = 30
banana = 20
print(apple, banana, 10)

# 보기 01: 파이썬 키워드 확인하기
import keyword

print(keyword.kwlist)

# 보기 02: 스크립트 문법 오류
# return = 217 # return은 파이썬의 키워드
# print(return)

# # 보기 03: 소문자 스타일의 객체명
# # 소문자 스타일 (lower_case_with_underscores, snake_case)
# customer_unique_visits
# http_server_error

# # 보기 04: 캡워드 스타일의 객체명
# # 캡워드 스타일 (CapWords, PascalCase, CamelCase)
# CustomerUniqueVisits
# HTTPServerError  # HTTP처럼 약어는 대문자로 표기

# # 보기 05: 혼합 스타일의 객체명
# # 혼합 스타일 (mixedCase)
# customerUniqueVisits
# HTTPServerError  # HTTP는 원래 대문자라 그대로 표기

# 추리하기 01
a = 2
b = 2.0
c = 2.00
d = 2.000
print(a, b, c, d)

# 추리하기 02
a = 0.310
b = 0.3100
c = 00.31
print(a, b, c)

# 추리하기 03
a = 15.0  # 15.
b = 0.8  # .8
print(a, b)

# 추리하기 04: 정수와 정수 간의 사칙 연산
# 산술 연산자 이해하기
a = 6
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a**b)

# 추리하기 05: 실수와 정수 간의 사칙 연산
a = 7.0
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a**b)

# 추리하기 06: 실수와 실수 간의 사칙 연산
a = 7.0
b = 3.0
print(a + b, a - b, a * b, a / b, a // b, a % b, a**b)

# 정리하기 01
a = 7
b = 3
print(a // b, a % b, a**b)

# 정리하기 02
a = 1 + 2 - 3 * 4
print(a)

# 정리하기 03
a = (1 + 2 - 3) * 4
print(a)

# 정리하기 04
# 제자리 연산
a = 10
a = a + 1
print(a)

# 정리하기 05
a = 10
a += 1  # a = a + 1
print(a)
