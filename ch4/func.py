### func.py

## structure
'''
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2
    ...
'''


def add(a: int, b: int) -> int:
    return a + b


# 이 함수의 이름은 add이고 입력으로 2개의 값을 받으며
# 반환값(출력값)은 2개의 입력값을 더한 값이다.

a = 3
b = 4
c = add(a, b)
print(c)  # 7


## parameters and arguments
# 매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 경우가 많다.
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수이고
# 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.
def add(a: int, b: int) -> int:  # a, b는 매개변수
    return a + b


print(add(3, 4))  # 3,4는 인수

## function types based on input and return values
# 함수는 들어온 입력값을 받은 후 어떤 처리를 하여 적절한 값을 반환해 준다.
# 함수의 형태는 입력값과 반환값의 존재 유무에 따라 4가지 유형으로 나뉜다.

# common function
# 입력값이 있고 반환값이 있는 함수가 일반적인 함수이다.
'''
def 함수_이름(매개변수):
    수행할_문장
    ...
    return 반환값 
'''


def add(a, b):
    result = a + b
    return result


# 이 함수를 사용하는 방법은 다음과 같다.
a = add(3, 4)
print(a)  # 7


# function without input values
# 입력값이 없는 함수는 다음과 같다.
def say():
    return 'Hi'


a = say()
print(a)  # Hi
# 위 함수를 사용하기 위해서는 say()처럼 괄호 안에 아무런 값도 넣지 않아야 한다.
# 이 함수는 입력값은 없지만, 반환값으로 "Hi"라는 문자열을 반환한다.
'''
반환값을_받을_변수 = 함수_이름()
'''


# function without output values
# 반환값이 없는 함수는 다음과 같다.
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


add(3, 4)
# 즉, 반환값이 없는 함수는 다음과 같이 사용된다.
'''
함수_이름(입력_인수1, 입력_인수2, ...)
'''


# function with no input or return value
# 입력값도, 반환값도 없는 함수는 다음과 같다.
def say():
    print('Hi')


say()

# 즉, 입력값도, 반환값도 없는 함수는 다음과 같이 사용한다.
'''
함수_이름()
'''


# calling by specifying parameters
# 함수를 호출할 때 매개변수를 지정할 수도 있다.
def sub(a, b):
    return a - b


# 2개의 숫자를 입력받은 후 첫 번째 수에서 두 번째 수를 뺄셈하여 반환하는 sub 함수이다.
# 다음과 같이 매개변수를 지정하여 사용할 수도 있다.
result = sub(a=7, b=3)
print(result)  # 4

# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.
result = sub(b=5, a=3)
print(result)  # -2

# what if you don't know how many input values there will be?
# 입력값이 여러 개일 때 그 입력값을 모두 더해 주는 함수를 생각해 보자.
# 하지만 몇 개가 입력될지 모를 때는 어떻게 해야 할까?
# 이런 문제를 해결하기 위해 다음과 같은 방법을 제공한다.
'''
def 함수_이름(*매개변수):
    수행할_문장
    ...
'''


# 매개변수 부분이 *매개변수로 변경되었다.

# creating a function that takes multiple input values
# 다음 예를 통해 여러 개의 입력값을 모두 더하는 함수를 만들어보자.
def add_many(*args: int):
    result = 0
    for i in args:
        result += i
    return result


# 위에서 만든 add_many 함수는 입력값이 몇 개이든 상관없다.
# *args처럼 매개변수 이름 앞에 *를 붙이면 입력값을 전부 튜플로 만들어주기 때문이다.
'''
args는 인수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용한다.
'''

result = add_many(1, 2, 3)
print(result)  # 6

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)  # 55


# 여러 개의 입력을 처리할 때
# def add_many(*args)처럼 함수의 매개변수로 *args 하나만 사용할 수 있는건 아니다.
def add_mul(choice: str, *args: int):
    result = 0
    if choice == 'add':
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result


# add_mul 함수는 여러 개의 입력값을 의미하는 *args 매개변수 앞에 choice 매개변수가 추가되어 있다.
result = add_mul('add', 1, 2, 3, 4, 5)
print(result)  # 15
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)  # 120


## kwargs. keyword parameters
# 키워드 매개변수는 함수 호출 시 키워드=값 형태로 전달하는 매개변수를 받을 때 사용한다.
# 키워드 매개변수를 사용할 떄는 매개변수 앞에 별 2개(**)를 붙인다.
def print_kwargs(**kwargs):
    print(kwargs)


# print_kwargs는 입력받은 키워드 매개변수들을 딕셔너리 형태로 출력하는 함수이다.
print_kwargs(a=1)
# { 'a': 1 }
print_kwargs(name="foo", age=3)
# { 'name': 'foo', 'age': 3 }
print_kwargs(name="홍길동", age=25, city="서울", job="개발자")


# { 'name': '홍길동', 'age': 25, 'city': '서울', 'job': '개발자' }

# 즉, **kwargs처럼 매개변수 이름 앞에 **를 붙이면 매개변수 kwargs는 딕셔너리가 된다.
# 키워드 매개변수의 실용적인 예를 살펴보자.
def create_profile(**info):
    print('=== 프로필 정보 ===')
    for key, value in info.items():
        print(f'{key}: {value}')


create_profile(이름="김철수", 나이=30, 직업="프로그래머", 취미="독서")


# === 프로필 정보 ===
# 이름: 김철수
# 나이: 30
# 직업: 프로그래머
# 취미: 독서

# 일반 매개변수, 가변 매개변수(*args), 키워드 매개변수(**kwargs)를 모두 함께 사용할 수 있다.
# 이때 순서는 다음과 같아야 한다.
def mixed_function(name, *args, **kwargs):
    print(f'이름: {name}')
    print(f'추가 인수들: {args}')
    print(f'키워드 인수들: {kwargs}')


mixed_function('홍길동', 1, 2, 3, age=25, city='서울')


# 이름: 홍길동
# 추가 인수들: (1, 2, 3)
# 키워드 인수들: {'age': 25, 'city': '서울'}

## the return value of a function is always one
# 함수의 리턴 값은 언제나 하나이다.
def add_and_mul(a: int, b: int):
    return a + b, a * b


# add_and_mul은 2개의 입력 인수를 받아 더한 값과 곱한 값을 반환하는 함수이다.
result = add_and_mul(3, 4)
print(result)  # (7, 12) 튜플
# 즉, 결과값으로 하나의 (7, 12)라는 튜플 값을 가지게 되는 것이다.
# 만약 분리해서 받고 싶다면 다음과 같이 하면 된다.
(result1, result2) = add_and_mul(3, 4)
print(result1)  # 7
print(result2)  # 12


# 다음과 같은 의문이 생길 수도 있다.
def add_and_mul(a: int, b: int):
    return a + b
    return a * b


print(add_and_mul(2, 3))  # 5


# 즉, 함수는 return 문을 만나는 순간, 반환값을 반환한 다음 함수를 빠져나간다.
# 따라서 다음 함수와 완전히 동일하다.
def add_and_mul(a: int, b: int):
    return a + b


## preset initial values for parameters
# 매개변수에 초깃값을 미리 설정해줄 수도 있다.
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나의 나이는 %d 입니다." % age)
    if man:
        print("나는 남자 입니다.")
    else:
        print("나는 여자 입니다.")


# 위를 보면 man=True 처럼 매개변수에 초깃값을 넣어주었다.
# 따라서 위 함수는 다음과 같이 사용할 수 있다.
say_myself("박응용", 27)
# 나의 이름은 박응용 입니다.
# 나의 나이는 27 입니다.
# 나는 남자 입니다.
say_myself("박응용", 27, True)
# 나의 이름은 박응용 입니다.
# 나의 나이는 27 입니다.
# 나는 남자 입니다.

# man의 초깃값이 True이기 때문에 위의 예에서는 동일한 결과를 출력하는 것을 확인할 수 있다.
say_myself("박응용", 27, False)

# 나의 이름은 박응용 입니다.
# 나의 나이는 27 입니다.
# 나는 여자 입니다.

# 하지만 초깃값을 설정할 때 주의할 것이 하나 있다.
'''
def say_myself(name, man=True, age):
    print("나의 이름은 %s 입니다." % name)
    print("나의 나이는 %d 입니다." % age)
    if man:
        print("나는 남자 입니다.")
    else:
        print("나는 여자 입니다.")
'''
#    def say_myself(name, man=True, age):
#                                   ^^^
# SyntaxError: parameter without a default follows parameter with a default
# 위와 같이 에러가 발생하는 것을 확인할 수 있다.

# scope of variables declared within a function
# 함수 안에서 사용할 변수의 이름을 함수 밖에서도 동일하게 사용하면 어떻게 될까?
a = 1


def vartest(a):
    a += 1


vartest(a)
print(a)  # 1


# 2가 출력될 것 같지만 1이 출력된다.
# 이유는 함수 안에서 사용하는 매개변수는 함수 안에서만 사용하는 "함수만의 변수"이기 때문이다.
# 즉 def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수일 뿐, 함수 밖의 변수 a와는 전혀 상관 없다.
def vartest(hello):
    hello += 1


# 즉, 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관없다는 뜻이다.
def vartest(z):
    z += 1


vartest(3)
# print(z)
#    print(z)
#          ^
# NameError: name 'z' is not defined

## How to change a variable outside a function from within a function
# 그렇다면 vartest라는 함수를 사용해서 함수 밖의 변수 a를 1만큼 증가할 수 있는 방법은 없을까?

# return 사용하기
a = 1


def vartest(a):
    a += 1
    return a


a = vartest(a)
print(a)  # 2

# global 사용하기
a = 1


def vartest():
    global a
    a += 1


vartest()
print(a)  # 2

## lambda
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다.
# 사용법은 다음과 같다.
'''
함수_이름 = lambda 매개변수1, 매개변수2, ...: 매개변수를_이용한_표현식
'''
add = lambda a, b: a + b
result = add(3, 4)
print(result)  # 7


# lambda로 만든 함수는 return 명령어가 없어도 표현식의 결괏값을 반환한다.
# 위의 lambda 함수는 아래와 완전히 동일하다.
def add(a, b):
    return a + b


## Docstring of function
# 함수에 대한 설명을 문서화하는 방법이 독스트링이다.
# 함수의 첫 번째 줄에 삼중 따옴표를 둘러싼 문자열로 작성하면 된다.
def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자

    Returns:
    int, float: 두 숫자의 합
    """
    return a + b


print(add.__doc__)

# 두 숫자를 더하는 함수
#
# Parameters:
# a (int, float): 첫 번째 숫자
# b (int, float): 두 번째 숫자
#
# Returns:
# int, float: 두 숫자의 합
