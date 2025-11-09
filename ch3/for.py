### for.py
# while 문과 비슷한 반복문인 for 문은 문장 구조가 한눈에 들어온다는 장점이 있다.

## structure
# for 문의 기본 구조는 다음과 같다
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수갱할_문장1
    수갱할_문장2
    ...
'''
# 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수가 대입되어
# 수행할_문장1, 수행할_문장2 등이 수행된다.

## understanding the for loop through examples
# 1. a typical for statement
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# one
# two
# three

# 2. Use of various for statement
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# 3. application of for statement
'''총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다.'''
marks = [90, 25, 67, 45, 80]
for mark in marks:
    print(f'{mark} : {'합격' if mark >= 60 else '불합격'}')

## for, continue statements
# while 문에서 사용했던 continue 문을 for 문에서도 사용할 수 있다.
# 마찬가지로 continue 문을 통해 for 문의 맨 처음으로 돌아갈 수 있다.
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print('%d번 학생 축하합니다. 합격입니다.' % number)
# 1번 학생 축하합니다. 합격입니다.
# 3번 학생 축하합니다. 합격입니다.
# 5번 학생 축하합니다. 합격입니다.

## range function
# for 문은 숫자 리스트를 자동으로 만들어주는 range 함수와 함께 사용하는 경우가 많다.
# 다음은 range 함수의 간단한 사용법이다.
a = range(10)
print(a)
# range(0, 10)
# 이는 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.
a = range(1, 11)
print(a)
# range(1, 11)
# 따라서 이는 1부터 10 까지의 숫자가를 초함한다.

add = 0
for i in range(1, 11):
    add += i

print(add)
# 55
# 1 ~ 10의 합

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

## multiplication tables using for and range
for i in range(2, 10):
    for j in range(2, 10):
        print(i * j, end=" ")
    print('')

## using list comprehensions
# 리스트 안에 for 문을 포함하는 리스트 컴프리헨션(list comprehension)을 사용하면
# 좀 더 편리하고 직관적인 프로그램을 만들 수 있다.
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)  # [3, 6, 9, 12]

# 만약 [1,2,3,4] 중에서 짝수에만 3을 곱하여 담고 싶다면
# 리스트 컴프리엔션 안에 if 조건문을 사용한다.
a = [1, 2, 3, 4]
reuslt = [num * 3 for num in a if num % 2 == 0]

# 리스트 컴프리엔션의 문법은 다음과 같다.
'''
[표현식 for 항목 in 반복_기능_객체 if 조건문]
'''
# 조금 복잡하지만 for 문을 2개 이상 사용하는 것도 가능하다.
'''
[표현식 for 항복1 in 반복_기능_객체_1 if 조건문1
    for 항목2 in 반복_기능_객체_2 if 조건문2
    ...
    for 항목n in 반복_기능_객체_n if 조건문n]
'''
# 구구단을 예시로 들면 다음과 같다.
result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
print(result)

## for, break statements
# while 문과 마찬가지로 for 문에서도 break 문을 사용할 수 있다.
# for 문을 강제적으로 빠져나가고 싶을 때 사용한다.
for i in range(10):
    if i == 5:
        break
    print(i)

## for-else statement
# while 문과 마찬가지로 for-else 문을 사용할 수 있다.
# break로 빠져나가지 않았을 경우 else 절이 실행된다.
for i in range(5):
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

# 하지만 break 문으로 빠져나가면 else 절은 실행되지 않는다.
for i in range(5):
    if i == 3:
        break;
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

## using the enumerate function
# 리스트의 순서(인덱스)와 값을 함께 구하고 싶을 때는 enumerate 함수를 사용하면 편리하다.
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# enumerate는 0부터 시작하는 인덱스 번호를 자동으로 생성해준다.
# 시작 번호를 변경하고 싶다면 다음과 같이 사용할 수 있다.
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")
# 1: apple
# 2: banana
# 3: orange

## iterating through multiple lists using the zip function
# 2개 이상의 리스트를 동시에 순회하고 싶을 때는 zip 함수를 사용한다.
names = ['홍길동', '김철수', '이영회']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")
# 홍길동: 85점
# 김철수: 92점
# 이영회: 78점

# 3개 이상의 리스트도 함께 순회할 수 있다.
names = ['홍길동', '김철수', '이영회']
korean = [85, 92, 78]
english = [90, 88, 95]
for name, kor, eng in zip(names, korean, english):
    print(f"{name}: {kor}점, {eng}점")
# 홍길동: 85점, 90점
# 김철수: 92점, 88점
# 이영회: 78점, 95점
