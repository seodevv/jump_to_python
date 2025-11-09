### example.py
## Q1 조건문의 참과 거짓
# 다음 코드의 결과값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')

# shirt

## Q2 3의 배수의 합 구하기
# while 문을 사용해 1 부터 1000 까지의 자연수 중 3의 배수의 합을 구해 보자.
n = 0
sum = 0
while n < 1000:
    n += 1
    if n % 3 == 0:
        sum += n

print(sum)

## Q3 별 표시하기
# while 문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자.
# *
# **
# ***
# ****
# *****
start = '*'
n = 0
while True:
    n += 1
    if n > 5: break;
    print(start * n)

## Q4 1 부터 100 까지 출력하기
# for 문을 사용해 1 부터 100 까지의 숫자를 출력해 보자.
for i in range(100):
    print(i + 1)

## Q5 평균 점수 구하기
# A 학급에 총 10 명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for 문을 사용하여 A 학급의 평균 점수를 구해 보자.
sum = 0
for score in scores:
    sum += score

print(f'이 학급의 평균 점수는 {sum / len(scores)}입니다.')

## Q6 리스트 컴프리헨션 사용하기
# 다음 소스 코드는 리스트의 요소 중에서 홀수만 골라 2를 곱한 값을 result 리스트에 담는 예제이다.
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
# 이 코드를 리스트 컴프리헨션을 사용하여 표현해 보자.
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print(result)
