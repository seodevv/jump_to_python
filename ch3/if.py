### if.py

## why is if necessary?
# "돈이 있으면 택시를 타고, 돈이 없으면 걸어간다."
# 실생활에서도 그렇지만 프로그래밍도 위 문장처럼 주어진 조건을 판단하여 상황에 맞게 처리해야되는 경우가 생긴다.
# 위와 같은 상황을 다음과 같이 표현할 수 있다.
money = True
if money:
    print("택시를 타고 가라!")
else:
    print("걸어 가라!")

# "택시를 타고 가라!"
# money가 True이므로 참이다.
# 따라서 if 문 다음 문장이 수행되어 "택시를 타고 가라!"가 출력된다.

## basic structure
# 다음은 if와 else를 사용한 조건문의 기본 구조다.
'''
if 조건문:
    수행할_문장1
    수행할_문장2
    ...
else:
    수행할_문장A
    수행할_문장B
    ...
'''
# 조건문이 참이면 수행할_문장1, 2, ...을 수행한다.
# 조건문이 거짓이면 수행할_문장A, B, ...을 수행한다.

## indentation
# if문을 만들 때는 if 조건문: 다음 들여쓰기(indentation)을 해야 한다.
'''
if 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
'''

# 다음처럼 작성하면 오류가 발생한다.
'''
if 조건문:
    수행할_문장1
수행할_문장2
    수행할_문장3
'''
'''
money = True
if money:
    print('택시 ')
print('타고 ')
    print('가라!')
'''
# IndentationError: unexpected indent
# 위와 같이 들여쓰기 오류가 발생하는 것을 확인할 수 있다.
# 커뮤니티에선 공백 문자 4개를 사용하는 것을 권장한다고 한다.
# 요즘 에디터에서도 탭을 사용해도 공백 문자로 치환된다.

## What is a conditional statement?
# if 조건문에서 '조건문' 이란 참과 거짓을 판단하는 문장이다.
money = True
if money:
    print('택시')
# money가 True이기 때문에 조건이 참이 되어 if 문 다음 문장을 수행한다.

## comparison operator
# 이번에는 조건문에 비교 연산자(<, > , ==, !=, >=, <=)를 쓰는 방법에 대해 알아본다.
'''
비교연산자   설명
x < y       x가 y보다 작다.
x > y       x가 y보다 크다.
x == y      x와 y가 같다.
x != y      x와 y가 같지 않다.
x >= y      x가 y보다 크거나 같다.
x <= y      x가 y보다 작거나 같다.
'''

x = 3
y = 2
print(x > y)  # True
# 이 조건문은 참이기 때문에 True를 반환한다.

print(x < y)  # False
# 이 조건문은 거짓이기 때문에 False를 반환한다.

print(x != y)  # True
# x와 y는 같지 않기 때문에 True를 반환한다.

money = 2000
if money >= 3000:
    print("택시를 타고 가자!")
else:
    print("걸어 가자!")

# "걸어 가자!"
# money는 3000보다 크거나 작지 않기 때문에 False를 반환하여 "걸어 가자!"가 출력된다.

## and, or, not
# 조건을 판단하기 위해 사용하는 논리 연산자(logical operator)로는 and, or, not이 있다.
'''
연산자     설명
x or y    x와 y 둘 중 하나만 참이어도 참이다.
x and y   x와 y 모두 참이어야 참이다.
not x     x가 거짓이면 참이다.  
'''

# 다음 예를 통해 or 연산자의 사용법을 알아본다.
# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
card = True
if (money >= 3000 or card == True):
    print("택시를 타고 가자!")
else:
    print("걸어 가자!")

# "택시를 타고 가자!"

## in, not in
# 파이썬에는 다른 프로그래밍 언어에서 쉽게 볼 수 었는 조건문도 제공한다.
'''
in              not in
x in 리스트       x not in 리스트
x in 튜플         x not in 튜플
x in 문자열       x not in 문자열
'''
# 영어 단어 in의 뜻이 '~안에' 라는 것을 생각해 보면 다음 예가 쉽게 이해 될 것이다.
print(1 in [1, 2, 3])  # True
# 리스트 안에 1이 있으므로 True
print(1 not in [1, 2, 3])  # False
# 리스트 안에 1이 없으므로 False

# 리스트와 같이 튜플, 문자열도 가능하다.
print('a' in ('a', 'b', 'c'))  # True
print('j' not in 'python')  # True

# 다음 예제를 적용해보자.
'''만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.'''
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가자!')
else:
    print('걸어 가자!')

# '택시를 타고 가자!'

# 만약 조건문에서 아무것도 하고 싶지 않을 때가 있다.
# 이런 경우에는 pass를 사용하면 된다.
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

## elif to judge various conditions
# if와 else만으로 다양한 조건을 판단하기 어렵다.
# 다음 예를 보더라도 if와 else만으로 조건을 판단하는데 어려움을 겪게 된다.
'''주머니에 돈이 있으면 택시를 타고 가고, 
주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 
돈도 없고 카드도 없으면 걸어가라.'''
# 위 문장을 보면 조건을 판단하는 부분이 두 군데가 있다.
# if와 else만으로 위 문장을 표현하려면 다음과 같이 할 수 있다.
pocket = ['paper', 'cellphone']
if 'money' in pocket:
    print('택시를 타고 가라!')
else:
    if 'card' in pocket:
        print('택시를 타고 가라!')
    else:
        print('걸어 가라!')

# 걸어 가라!
# 언뜻 보기에도 어렵고 산만한 느낌이다.
# 이런 다중 조건일 경우에는 elif를 사용하면 된다.

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라!')
elif card:
    print('택시를 타고 가라!')
else:
    print('걸어 가라!')

# '택시를 타고 가라!'

# 즉, elif는 이전 조건문이 거짓일 때 수행된다.
# if, elif, else를 모두 사용할 때 기본 구조는 다음과 같다.
'''
if 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
...
else:
    수행할_문장1
    수행할_문장2
    ...
'''

## chaining of comparison operator
# 수학에서처럼 비교 연산자를 연쇄적으로 사용할 수 있다.
x = 5
print(1 < x < 10)  # True
print(10 <= x <= 20)  # False

# 이는 다음과 같이 쓰는 것과 같다.
print(1 < x and x < 10)  # True
print(10 <= x and x <= 20)  # False

## conditional expression
# 때로는 조건에 따라 변수에 서로 다른 값을 대입하고 싶을 때가 있다.
'''점수가 60점 이상이면 "합격", 미만이면 "불합격"이라는 메시지를 저장한다.'''
score = 85
if score >= 60:
    result = "합격"
else:
    result = "불합격"
print(result)  # 합격

# 이런 간단한 조건 분기는 파이썬의 조건부 표현식을 사용하면 한 줄로 표현할 수 있다.
score = 85
result = "합격" if score >= 60 else "불합격"
print(result)  # 합격

# 조건부 표현식의 기본 형태는 다음과 같다.
'''
변수 = 참일_때_값 if 조건 else 거짓일_때_값
'''
# 이를 해석하면 "조건이 참이면 '참일 때 값'을, 거짓이면 '거짓일 때 값'을 변수에 대입한다는 의미이다.
# 더 많은 예제를 살펴보자.
age = 19
status = "성인" if age >= 18 else "미성년"
print(status)  # 성인

temperature = 25
weather = "따뜻함" if temperature > 20 else "추움"
print(weather)  # 따뜻함

money = 1500
transportation = "버스" if money >= 1000 else "도보"
print(transportation)  # 버스

# 조건부 표현식은 코드를 간결하게 만들어 주지만, 너무 복잡한 조건이나 긴 표현식에는 사용하지 않는 것이 좋다.
# 가독성이 떨어질 수 있기 때문이다.
