### bool.py
# 불(bool) 자료형은 참(True)와 거짓(False)를 나타내는 자료형이다.
# True: 참
# False: 거짓
# 첫 문자를 항상 대문자로 작성해야 한다.

## Usage
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

print(1 == 1)  # True
print(2 > 1)  # True
print(2 < 1)  # False

# True? False?
"python"  # True
''  # False
[1, 2, 3]  # True
[]  # False
(1, 2, 3)  # True
()  # False
{'a': 1}  # True
{}  # False
1  # True
0  # False
None  # False

a = [1, 2, 3, 4]
while a:
    print(a.pop())
# 4
# 3
# 2
# 1

if []:
    print('참')
else:
    print("거짓")
# 거짓

if [1, 2, 3]:
    print("참")
else:
    print("거짓")
# 참

## caculation
print(bool('python'))  # True
print(bool([]))  # False
print(bool(0))  # False
print(bool(3))  # True

## Logical
# and
True and True  # True
True and False  # False
False and True  # False
False and False  # False

# or
True or True  # True
True or False  # True
False or True  # True
False or False  # False

# not
not True  # False
not False  # True
not 1  # False
not 0  # True

# example
x = 5
y = 10
print(x > 0 and y > 0)  # True
print(x > 10 or y > 5)  # True
print(not (x > y))  # True
