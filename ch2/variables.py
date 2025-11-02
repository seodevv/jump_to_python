### variables.py

## how to create variables?
a = 1
b = 'python'
c = [1, 2, 3]
# 변수_이름 = 변수에_저장할_값
# 다른 프로그래밍 언어(C, JAVA)에서는 변수를 만들 때 자료형의 타입을 직접 지정해주어야 한다.
# 하지만 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형의 타입을 지정하여 편리하다.

## variables naming convention
# 1. 영문자, 숫자, 언더스코어(_)만 사용할 수 있다.
# 2. 숫자로 시작할 수 없다.
# 3. 예약어는 사용할 수 없다.
# 4. 대소문자를 구분한다.

# correct
name = '홍길동'
age = 25
user_name = "gildong"
userName = "gildong"
_private = "비공개"
count1 = 10

# incorrect
# 1name = "홍길동"
# SyntaxError: invalid decimal literal

# user - name = "홍길동"
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

# if = 10
# SyntaxError: invalid syntax

## resolved word
# False, None, True, and, as, assert, break, class, continue, def,
# del, elif, else, except, finally, for, from, global, if, import,
# in, is, lambda, nonlocal, not, or, pass, raise, return, try,
# while, with, yield

## recommendation
# 의미가 명확한 이름을 사용한다.
# snake_case (단어 사이에 언더스코어)를 권장한다.
# 너무 짧거나 긴 이름은 피한다.

# correct
student_name = "김철수"
total_score = 95
user_age = 20

# incorrect
a = "김철수"
studentNameFromKorea = "김철수"  # too long

## What is the variable?
# 변수는 객체를 가리키는 것이다.
# 객체란 자료형의 데이터(값)이다.
a = [1, 2, 3]
# [1,2,3] 값을 가지는 리스트 데이터(객체)가 자동으로 메모리에 생성된다.
# 변수 a는 [1,2,3] 리스트가 저장된 메모리의 주소를 가르키게 된다.

# a 변수가 가르키는 메모리의 주소는 다음과 같이 확인할 수 있다.
a = [1, 2, 3]
print(id(a))
# id 함수는 변수가 가르키고 있는 객체의 주소 값을 반환하는 내장 함수다.

## when you want to copy a list
a = [1, 2, 3]
b = a
print(id(a))  # 1993779951488
print(id(b))  # 1993779951488
print(a is b)  # True
# id(a)와 id(b)가 동일하다는 것을 확인할 수 있다.

a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 4, 3]

## Deep copy
# use [:]
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)  # [1,4,3]
print(b)  # [1,2,3]
print(a is b)  # False

# use copy module
from copy import copy

a = [1, 2, 3]
b = copy(a)  # b = a[:]
a[1] = 4
print(a)  # [1,4,3]
print(b)  # [1,2,3]
print(a is b)  # False

## several ways to create variables
a, b = ('python', 'life')
print(a)  # python
print(b)  # life
(a, b) = ('python', 'life')
print(a)  # python
print(b)  # life

[a, b] = ['python', 'life']
print(a)  # python
print(b)  # life

a = b = 'python'
print(a)  # python
print(b)  # python

a = 3
b = 5
a, b = b, a  # omg!
print(a)  # 5
print(b)  # 3
