### file.py

# create file
# f = open("새파일.txt", 'w')
# f.close()
# 프로그램을 실행하면 새파일.txt가 생성된 것을 확인할 수 있다.
# open은 파이썬 내장 함수이다.
# open 함수는 다음과 같이 '파일 이름'과 '파일 열기 모드'를 입력값으로 받고 결과값으로 파일 객체를 반환한다.
'''
파일_객체 = open(파일_이름, 파일_열기_모드)
'''
from unittest import enterModuleContext

# 파일 열기 모드는 다음과 같은 것들이 있다.
'''
파일열기모드      설명
r               읽기 모드: 파일을 읽기만 할 때 사용한다.
w               쓰기 모드: 파일에 내용을 쓸 때 사용한다.
a               추가 모드: 파일의 마지막에 새로운 내용을 추가할 때 사용한다.
'''
# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용은 모두 사라진다.
# 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.

# 만약 "새파일.txt" 파일을 C:/doit 디렉토리에 생성하고 싶다면 다음과 같이 작성하면 된다.
# f = open('C:/Users/bluea/Documents/develope/python/jump_to_python/ch4/새파일_2.txt', 'w')
# f.close()
# f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 한다.
# 생략해도 된다. 프로그램을 종료할 때 파이썬이 열려 있는 파일의 객체를 자동으로 닫아 주기 때문이다.
# 하지만 close()를 사용해서 열려 있는 파일을 직접 닫아 주는 것이 좋다.

# 파이썬에서는 경로를 표시할 때 다음과 같이 사용할 수 있다.
# 슬래시(/) - "C:/Users/새파일.txt"
# 역슬래시(\\) - "C:\\Users\\새파일.txt"
# r 문자(raw string) - r"C:\doit\새파일.txt"

## open the file in write mode and write the contents
# 쓰기 모드로 연 후, 문자열 데이터를 파일에 직접 써보자.
f = open('새파일.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

## several ways to read a file
# 파이썬에는 파일을 읽는 방법이 여러 가지가 있다.

# using readline function
# 첫 번째는 realine 함수를 사용하는 것이다.
f = open('새파일.txt', 'r', encoding='utf-8')
line = f.readline()
print(line)
f.close()
# readline.txt 파일을 읽기 모드로 연 후 readline()을 사용하여 파일의 첫 번째 줄을 읽어 출력하는 예제이다.
# 만약 모든 줄을 읽고 싶다면 다음과 같이 작성하면 된다.
f = open('새파일.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
f.close()
print('')

# using readlines function
# 두 번째 방법은 readlines 함수를 사용하는 것이다.
f = open("새파일.txt", 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()
print('')
# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 반환한다.
# 따라서 위 예에서는 lines는 리스트 ['1번째 줄입니다.\n","2번째 줄입니다.\n", ... "10번째 줄입니다.\n"]

# 줄 바꿈(\n) 문자를 제거하고 싶으면 strip 함수를 사용하면 된다.
f = open("새파일.txt", 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()
print('')

# using read function
# 세 번째는 read 함수를 사용하는 방법이다.
f = open('새파일.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()

# using file objects with for loops
# 네 번째는 파일 객체를 for 문과 함께 사용하는 방법이다.
f = open('새파일.txt', 'r', encoding='utf-8')
for line in f:
    print(line.strip())
f.close()
print('')

# add new content to a file
# 쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 내용이 다 사라진다.
# 하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야할 경우도 있다.
# 이런 경우에는 파일을 추가 모드('a')로 열면 된다.
'''
f = open('새파일.txt', 'a', encoding='utf-8')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

f = open("새파일.txt", 'r', encoding='utf-8')
for line in f:
    print(line.strip())
f.close()
print('')
# 새파일.txt 파일에 11번째 줄입니다. ... 19번째 줄입니다. 가 추가된 것을 확인할 수 있다.

# use with the statement
# 지금까지 살펴본 에제를 보면 항상 다음과 같은 방식으로 파일을 열고 닫은 것을 알 수 있다.
f = open('foo.txt', 'w', encoding='utf-8')
f.write('Life is too short, you need python')
f.close()
# 파일을 열면(open) 항상 닫아(close) 주어야 한다.
# 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까?
# with 문이 바로 이런 역할을 해준다.
with open('foo.txt', 'w', encoding='utf-8') as f:
    f.write('Life is too short, you need python')


# 위와 같이 with 문을 사용하면 with 블록을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힌다.

# with statement and scope rules
# 파이썬에서 with 문 내에서 선언된 변수는 with 블록을 벗어난 후에도 접근할 수 있다.
# 이는 파이썬의 스코프(유효 범위) 특성 때문이다.
# 파이썬에서는 함수 스코프와 블록 스코프가 다르게 동작한다.

# 1. 함수 스코프
# 함수 안에서 선언된 변수는 함수 밖에서 접근할 수 없다.
def my_function():
    func_var = "함수 안의 변수"


my_function()
# print(func_var)

# 2. 블록 스코프
# if, for, while, with 등의 블록 안에서 선언된 ㅂ ㅕㄴ수는 블록 밖에서도 접근할 수 있다.
if True:
    if_var = "if 블록 안의 변수"
print(if_var)  # if 블록 안의 변수

for i in range(3):
    loop_var = "반복문 안의 변수"
print(loop_var)  # 반복문 안의 변수

# 이와 가은 이유로 with 문에서도 블록 안에서 선언된 변수는 블록 밖에서도 접근할 수 있다.
with open('test.txt', 'w', encoding='utf-8') as f:
    content = "Hello, Python!"
    f.write(content)

print(content)  # Hello, Python!

# notice
# 한글이 포함된 파일을 다룰 떄는 인코딩을 명시하는 것이 좋다.
with open("한글파일.txt", 'w', encoding='utf-8') as f:
    f.write('안녕하세요. 파이썬!')

with open("한글파일.txt", 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)  # 안녕하세요. 파이썬!
