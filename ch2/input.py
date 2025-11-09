### input_output.py

## using user input
# 사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때는 input 을 사용한다.
# a = input()
# print(a)

## using prompt
'''
input("안내_문구")
'''
# number = input("숫자를 입력하세요: ")
# print(f'입력하신 숫자는 {number}입니다.')
# print(type(number))  # <class 'str'>
# 괄호 안의 입력한 문구가 프롬프트로 나타난다.
# input은 입력되는 모든 것을 문자열로 취급한다.

## convert input values to numbers
# input 함수는 항상 문자열을 반환하므로, 숫자 계산을 하려면 적절한 자료형으로 변환해야 한다.

# convert int
# age = input("나이를 입력하세요: ")
# age = int(age)
# print(f'당신의 내년 나이는 {age + 1}입니다.')

# convert float
# height = input("키를 입력하세요(cm): ")
# height = float(height)
# print(f'당신의 키는 {height / 100}m 입니다.')

# convert in one go
# age = int(input("나이를 입력하세요: "))
# print(type(age))  # <class 'int'>

# print learn more
# 지금까지 우리가 사용한 print 문의 용도는 데이터를 출력하는 것이었다.
# 데이터를 출력하는 print 문의 사용 예는 다음과 같다.
a = 123
print(a)  # 123
a = 'Python'
print(a)  # Python
a = [1, 2, 3]
print(a)  # [1,2,3]

# strings enclosed in double quotes are equivalent to the + operation
# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다.
print("life" "is" "too short")  # lifeistoo short
print("life" + "is" + "too short")  # lifeistoo short

# string spacing is done with commas
# 문자열 띄어쓰기는 쉼표로 한다.
print("life", "is", "too short")  # life is too short

# settings the delimiter with the sep parameter
# seq 매개변수로 구분자 설정하기
print("2025", "08", '17', sep="-")  # 2025-08-17
print("점프", "투", "파이썬", sep=" TO ")  # 점프 TO 투 TO 파이썬

# print the result on one line
# 한 줄에 결과값 출력하기
# 매개변수 end를 통해 끝 문자를 지정할 수 있다.
for i in range(10):
    print(i, end=' ')

# 0 1 2 3 4 5 6 7 8 9 9
# end 매개변수의 기본값은 줄바꿈(\n) 문자이다.

## tutorial: creating a simple calculator
print("=== 간단한 계산기 ===")

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')

if num2 != 0:
    print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('0으로 나눌 수 없습니다.')
