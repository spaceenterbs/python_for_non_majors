# 2.3. 문자열
# 문자열 만들기

# 문자열의 특성 이해하기
# 추리하기 01
# a = apple
# print(a)

# 추리하기 02
a = "apple"  # 'apple'
b = "apple"
print(a, type(a))
print(b, type(b))

# 추리하기 03
# a = ''apple''
# print(a)

# 추리하기 04
a = """apple"""
b = """apple"""
print(a, type(a))
print(b, type(b))

# 추리하기 05
# a = 'app'le'
# print(a)

# 추리하기 06
a = 'app"le'
b = "app'le"
print(a, b)

# 추리하기 07
a = """app'le"""  # '''app'le'''
b = """app"le"""
print(a, b)

# 추리하기 08
a = "app'le"  # 'app\'le'
b = 'app"le'  # "app\"le"
print(a, b)

# 응용하기 02
a = "이번 'Z 채널'의 bounce rate는 0.3입니다."  # '이번 \'채널\'의 bounce rate는 0.3입니다.'
b = "이번 'Z 채널'의 bounce rate는 0.3입니다."  # "이번 '채널'의 bounce rate는 0.3입니다."
c = """이번 'Z 채널'의 bounce rate는 0.3입니다."""  # '''이번 '채널'의 bounce rate는 0.3입니다.'''
print(a)
print(b)
print(c)

# 정리하기 01
address = "대한민국\n\t서울특별시\n\t\t서초구\n\t\t강남대로"
print(address)

# 정리하기 02
address = "대한민국\\서울특별시\\서초구"
print(address)

# 정리하기 03
reply0 = """{
id: 'apple',
date: '2023-10-02',
text: '싫어요',
score: 4,
}"""
print(reply0)

# 정리하기 04
"""
모듈 최초 생성일: 2023년 10월 2일
모듈 목적: 파이썬 테스트
"""
print("module test")

# 정리하기 05
# a = 10
# b = "10"
# print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 정리하기 06
# 주민등록번호 예시
print(930602 - 1234567)
print("930602-1234567")

# 정리하기 07
# print(065267) # SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# 정리하기 08
print("065267")

# 정리하기 09
