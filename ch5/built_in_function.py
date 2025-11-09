### built_in_function.py
# 이 섹션에서는 내장(built-in) 함수에 대해 살펴본다.

## abs
# 절대값을 반환하는 함수
print(abs(3))  # 3
print(abs(-3))  # 3

## all
# all(x)는 반복 가능한 데이터 x를 입력값으로 받으며,
# x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 반환한다.
print(all([1, 2, 3]))  # True
print(all([1, 2, 3, 0]))  # False
print(all([]))  # True

## any
# any(x)는 반복 가능한 데이터 x를 입력값으로 받으며,
# x의 요소 중 하나라도 참이 있으면 True를 반환하고, 모두 거짓일 때만 False를 반환한다.
print(any([1, 2, 3, 0]))  # True
print(any([0, ""]))  # False
print(any([]))  # False

## chr
# chr(i)는 유니코드 숫자 값을 받아 그 코드에 해당하는 문자를 반환하는 함수이다.
print(chr(97))  # a
print(chr(44032))  # 가

## dir
# dir은 객체가 지닌 변수나 함수를 보여 주는 함수이다.
print(dir([1, 2, 3]))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir({'1': 'a'}))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

## divmod
# divmod(a,b)는 2개의 숫자 a,b를 입력으로 받는다.
# a를 b로 나눈 몫과 나머지를 튜플로 반환한다.
print(divmod(7, 3))  # (2,1)

## enumerate
# enumerate는 "열거하다"라는 뜻이다.
# 이 함수는 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 반환한다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar

## eval
# eval(expression)은 문자열로 구성된 표현식을 입력으로 받아
# 해당 문자열을 실행한 결과값을 반환하는 함수이다.
print(eval('1+2'))  # 3
print(eval("'hi' + 'a'"))  # hia
print(eval('divmod(4,3)'))  # (1,1)


## filter
# filter란 '무엇인가를 걸러 낸다'라는 뜻으로, 기능도 비슷하다.
# 첫 번째 인수로 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다.
# 그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 반환값이 True인 것만 반환한다.


# positive.py
def positive(l: list[int]):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result


print(positive([1, -3, 2, 0, -5, 6]))  # [1,2,6]


# filter1.py
def positive(x):
    return x > 0


print(list(filter(positive, [1, -3, 2, 0, -5, 6])))  # [1,2,6]
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))  # [1,2,6]

## hex
# hex(x)는 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 반환하는 함수이다.
print(hex(234))  # 0xea
print(hex(3))  # 0x3

## id
# id(object)는 객체를 입력받아 객체의 고유 주소값(레퍼런스)를 반환하는 함수이다.
a = 3
print(id(3))  # 140704936326120
print(id(a))  # 140704936326120
b = a
print(id(b))  # 140704936326120

print(id(4))  # 140704936326152

## input
# input([prompt])는 사용자 입력을 받는 함수이다.
# 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.
a = input()  # hi
print(a)  # hi
b = input('Enter: ')  # Enter: hello
print(b)  # hello

## int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 반환하는 함수이다.
print(int('3'))  # 3
print(int(3.4))  # 3

# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 반환한다.
print(int('11', 2))  # 3
print(int('1A', 16))  # 26


## isinstance
# isinstance(object, class) 함수는
# 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받는다.
# 객체가 해당 클래스라면 True, 아니면 False를 반환한다.
class Person: pass


a = Person()
print(isinstance(a, Person))  # True
b = 3
print(isinstance(b, Person))  # False

## len
# len(s)는 입력값 s의 길이(요소의 전체 개수)를 반환하는 함수이다.
print(len('python'))  # 6
print(len([1, 2, 3]))  # 3
print(len((1, 'a')))  # 2

## list
# list(iterable)은 반복 가능한 데이터를 입력받아 리스트로 반환한다.
print(list('python'))  # ['p','y','t','h','o','n']
print(list((1, 2, 3)))  # [1,2,3]


## map
# map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
# map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 반환하는 함수이다.

# two_times.py
def two_times(numberList: list[int]):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times([1, 2, 3, 4])
print(result)  # [2,4,6,8]


# map 함수를 사용하면 다음처럼 바꿀 수도 있다.
def two_times(x):
    return x * 2


print(list(map(two_times, [1, 2, 3, 4])))  # [2,4,6,8]
print(list(map(lambda x: x * 2, [1, 2, 3, 4])))  # [2,4,6,8]
# 마찬가지로 lambda를 사용하면 간편하다.

## max
# max(iterable)은 인수로 반복 가능한 데이터를 입력받아 최대값을 반환한다.
print(max([1, 2, 3]))  # 3
print(max('python'))  # y

## min
# min(iterable)은 max 함수와 반대인 최소값을 반환한다.
print(min([1, 2, 3]))  # 3
print(min('python'))  # h

## oct
# oct(x)는 정수를 8진수 문자열로 반환한다.
print(oct(34))  # 0o42
print(oct(12345))  # 0o30071

## open
# open(filename, [mode])는 '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 반환한다.
'''
mode    설명
w       쓰기 모드
r       읽기 모드
a       추가 모드
b       바이너리 모드
'''
# b는 w, r, a와 함께 사요한다.
f = open('binary_file', 'rb')
f.close()

## ord
# ord(c)는 문자의 유니코드 숫자 값을 반환하는 함수이다.
print(ord('a'))  # 97
print(ord('가'))  # 44032

## pow
# pow(x,y)는 x를 y 제곱한 값을 반환한다.
print(pow(2, 4))  # 16
print(pow(3, 3))  # 27

## range
# range([start,] stop [,step])은 for 문과 함께 주로 사용하는 함수이다.
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환한다.

# 1. 인수가 하나일 경우
# 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
print(list(range(5)))  # [0,1,2,3,4]

# 2. 인수가 2개일 경우
# 시작 숫자와 끝 숫자를 나타낸다.
# 끝 숫자는 포함되지 않는다.
print(list(range(5, 10)))  # [5,6,7,8,9]

# 3. 인수가 3개일 경우
# 세 번째 인수는 숫자 사이의 거리를 말한다.
print(list(range(1, 10, 2)))  # [1,3,5,7,9]
print(list(range(0, -10, -1)))  # [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]

## round
# round(number [,ndigits])는 숫자를 반올림하여 반환하는 함수이다.
print(round(4.6))  # 5
print(round(4.2))  # 4

## sorted
# sorted(iterable)는 입력 데이터를 정렬한 후 그 결과를 리스트로 반환하는 함수이다.
print(sorted([3, 1, 2]))  # [1,2,3]
print(sorted(['a', 'c', 'b']))  # ['a','b','c']
print(sorted('zero'))  # ['e','o','r','z']
print(sorted((3, 2, 1)))  # (1,2,3)
# 리스트 자료형에도 sort 함수가 있다.
# 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬할 뿐,
# 정렬된 결과를 반환하지는 않는다.

## str
# str(object)는 문자열 형태로 객체를 변환하여 반환한다.
print(str(3))  # '3'
print(str('hi'))  # 'hi'

## sum
# sum(iterable)은 입력 데이터의 합을 반환한다.
print(sum([1, 2, 3]))  # 6
print(sum([4, 5, 6]))  # 15

## tuple
# tuple(iterable)은 반복 가능한 데이터를 튜플로 변환하여 반환하는 함수이다.
# 입력이 튜플인 경우 그대로 반환한다.
print(tuple('abc'))  # ('a', 'b', 'c')
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(tuple((1, 2, 3)))  # (1, 2, 3)

## type
# type(object)는 입력값의 자료형이 무엇인지 알려준다.
print(type('abc'))  # <class 'str'>
print(type([]))  # <class 'list'>
print(type(open('test', 'w')))  # <class '_io.TextIOWrapper'>

## zip
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 반환하는 함수이다.
print(list(zip([1, 2, 3], [4, 5, 6])))  # [(1,4), (2,5), (3,6)]
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))  # [(1,4,7), (2,5,8), (3,6,9)]
print(list(zip('abc', 'def')))  # [('a','d'), ('b','e'), ('c','f')]
