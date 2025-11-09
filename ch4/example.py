### example.py

## Q1 홀수, 짝수 판별하기
# 주어진 자연수가 홀수인지, 짝수인지 판별해 주는 함수 is_odd를 작성해보자.
# is_odd 함수는 홀수이면 True, 짝수이면 False를 리턴해야 한다.
def is_odd(num: int):
    return num % 2 == 0


print(is_odd(2))  # True
print(is_odd(5))  # False


## Q2 모든 입력의 평균값 구하기
# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자.
# 단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.
def avg_numbers(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print(avg_numbers(1, 2))  # 3
print(avg_numbers(1, 2, 3, 4, 5))  # 15

## Q3 프로그램 오류 수정하기 1
# 다음은 2개의 숫자를 입력받아 더한 후에 리턴하는 프로그램이다.
input1 = int(input("첫 번째 숫자를 입력하세요: "))
input2 = int(input("두 번째 숫자를 입력하세요: "))

total = input1 + input2
print("두 수의 합은 %s 입니다." % total)

## Q4 출력 결과가 다른 것은?
# 다음 중 출력 결과가 다른 하나는?
print('you''need''python')  # youneedpython
print('you' + 'need' + 'python')  # youneedpython
print('you', 'need', 'python')  # you need python
print(''.join(['you', 'need', 'python']))  # youneedpython

## Q5 프로그램 오류 수정하기 2
# 다음은 파일(test.txt)에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어 출력하는 프로그램이다.
f1 = open('test.txt', 'w', encoding='utf-8')
f1.write('Life is too short')
f1.close()  # 파일을 쓴 후 종료한다.

f2 = open('test.txt', 'r', encoding='utf-8')
print(f2.read())
f2.close()
# 이 프로그램은 우리가 예상한 "Life is too short"이라는 문장을 출력하지 않는다.
# 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해보자.


## Q6 사용자 입력 저장하기
# 사용자의 입력을 파일 (user_input.txt)에 저장하는 프로그램을 작성해보자.
# 단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
user_input = input("저장할 내용을 입력하세요: ")
f = open("user_input.txt", 'a', encoding='utf-8')
f.write(user_input)
f.write('\n')
f.close()

## Q7 파일의 문자열 바꾸기
# 다음과 같은 내용을 지닌 change_string.txt가 있다.
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어 저장해보자.
'''
Life is too short
you need java
'''
f = open('change_string.txt', 'r', encoding='utf-8')
body = f.read()
f.close()
body = body.replace('java', 'python')
f = open('change_string.txt', 'w', encoding='utf-8')
f.write(body)
f.close()

## Q8 입력값을 모두 더해 출력하기
# 다음과 같이 실행할 때 입력값을 모두 더해 출력하는 스크립트를 작성해보자.
'''
cd doit
python example.py 1 2 3 4 5 6 7 8 9 10
55
'''
import sys

args = sys.argv[1:]
result = 0
for arg in args:
    result += int(arg)

print(result)
