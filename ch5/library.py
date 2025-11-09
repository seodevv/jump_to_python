### library.py
# 파이썬 표준 라이브러리는 파이썬을 설치할 때 자동으로 설치된다.

## datetime.date
# datetime.date는 연, 월, 일로 날짜를 표현할 때 사용하는 함수이다.
import datetime

day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)
diff = day2 - day1
print(diff)  # 477
print(type(day1))  # <class 'datetime.date'>
print(type(diff))  # <class 'datetime.timedelta'>
# 간단한 뺄셈을 통하 두 날짜의 차이를 쉽게 확인할 수 있다.

day = datetime.date(2021, 12, 14)
print(day.weekday())  # 1
'''
값   설명
0   월
1   화
2   수
3   목
4   금
5   토
6   일
'''

print(day.isoweekday())  # 2
'''
값   설명
1   월
2   화
3   수
4   목
5   금
6   토
7   일
'''

## time
# 시간과 관련된 time 모듈에는 함수가 많다.
# 유용한 함수만 확인해보자.

## time.time
# UTC(universal time coordinated, 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 반환한다.
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환해 준다.
import time

print(time.time())  # 1762684479.8001173
print(type(time.time()))  # <class 'float'>

## time.localtime
# time.localtime은 time.time()이 반환한 실수값을 사용해 연, 월, 일, 시, 분, 초, ...의 형태로 바꿔준다.
localtime = time.localtime(time.time())
print(localtime)
# time.struct_time(tm_year=2025, tm_mon=11, tm_mday=9, tm_hour=19, tm_min=35, tm_sec=32, tm_wday=6, tm_yday=313, tm_isdst=0)
print(type(localtime))
# <class 'time.struct_time'>

## time.asctime
# time.asctime은 time.localtime이 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 반환한다.
asctime = time.asctime(time.localtime(time.time()))
print(asctime)
# Sun Nov  9 19:44:10 2025
print(type(asctime))
# <class 'str'>

## time.ctime
# time.asctime(time.localtime(time.time()))은 간단하게 time.ctime()으로 표시할 수 있다.
# ctime이 asctime과 다른 점은 항상 현재 시간만을 반환한다는 점이다.
print(time.ctime())
# Sun Nov  9 19:45:01 2025

## time.strftime
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 포맷 코드를 제공한다.
strfttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(strfttime)
# 2025-11-09 19:47:14
print(type(strfttime))
# <class 'str'>
'''
포맷코드    설명                        예
%a         요일의 준말                 Mon
%A         요일                       Monday
%b         달의 줄임말                  Jan
%B         달                         January
%c         날짜와 시간                  Thu May 25 10:13:52 2023
%d         일(day)                     [01,31]
%H         시간: 24시간                 [00,23]
%I         시간: 12시간                 [01,12]
%j         1년 중 누적 날짜              [001,366]
%m         달                          [01,12]
%M         분                          [01,59]
%p         AM or PM                    AM
%S         초                          [00,59]
%U         1년 중 누적 주(일요일 시작)     [00,53]
%w         숫자로 된 요일                [0(일), 6(토)]
%W         1년 중 누적 주(월요일 시작)     [00,53]
%x         현재 설정된 지역에 기반한 날짜    05/25/23
%X         현재 설정된 지역에 기반한 시간    17:22:21
%Y         연도                          2023
%Z         시간대                        대한민국 표준시
%%         문자 %                        %
%y         세기 부분을 제외한 연도          01
'''
import time

date = time.localtime(time.time())
print(time.strftime("%x", date))  # 11/09/25
print(time.strftime('%c', date))  # Sun Nov  9 20:04:03 2025

## time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다.
# 일정한 시간 간격을 두고 루프를 실행할 수 있다.
import time

for i in range(10):
    print(i)
    time.sleep(0.1)  # 0.1초
# 1초를 간격으로 0부터 9까지 숫자를 출력한다.

## math.gcd
# math.gcd 함수를 이용하면 최대 공약수(gcd, greatest common divisor)를 구할 수 있다.
# 파이썬 3.5 버전부터 사용할 수 있다.

'''
어린이집에서 사탕 60개, 초콜릿 100개, 젤리 80개를 준비했다. 
아이들이 서로 싸우지 않도록 똑같이 나누어 봉지에 담는다고 하면 최대 몇 봉지까지 만들 수 있을까? 
단, 사탕, 초콜릿, 젤리는 남기지 않고 모두 담도록 한다.
'''
import math

print(math.gcd(60, 100, 80))
# 20
# 파이썬 3.9 버전부터는 math.gcd에 여러 인수를 입력할 수 있다.
# 3.9 미만은 2개까지 허용된다.

## math.lcm
# math.lcm은 최소 공배수(lcm, least common multiple)을 구할 때 사용하는 함수이다.
# 파이썬 3.9 버전부터 사용할 수 있다.
'''
어느 버스 정류장에 시내버스는 15분마다 도착하고 마을버스는 25분마다 도착한다고 한다. 
오후 1시에 두 버스가 동시에 도착했다고 할 때 두 버스가 동시에 도착할 다음 시각을 알려면 어떻게 해야 할까?
'''
import math

print(math.lcm(15, 25))  # 75
# 2시 15분

## random
# random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다.
import random

print(random.random())
# 0.826918042190119
# 0.0 ~ 1.0 사이의 실수값이 반환된다.

print(random.randint(1, 10))
# 6
# 1 ~ 10 사이의 정수값이 반환된다.

print(random.randint(1, 55))
# 43
# 1 ~ 55 사이의 정수값이 반환된다.

# random_pop.py
import random


def random_pop(data: list[int]):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))


# 1
# 5
# 3
# 2
# 4

# random.choice를 사용하면 더 직관적으로 만들 수 있다.
def random_pop(data: list[int]):
    number = random.choice(data)
    data.remove(number)
    return number


# random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나 선택하여 반환된다.

# 리스트 항목을 무작위로 섞고 싶을 떄는 random.sample 함수를 사용하면 된다.
import random

data = [1, 2, 3, 4, 5]
print(random.sample(data, len(data)))
# [1,4,2,3,5]

## itertools.zip_longest
# itertools.zip_longest(*iterables, fillvalue=None) 함수는 zip 함수와 똑같이 동작한다.
# 하지만 itertools.zip_longest() 함수는 전달한 반복 기능 객체(*iterables)의 길이가 서로 다르다면
# 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 짧은 객체에 채울 수 있다.

# itertools_zip.py
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = zip(students, snacks)
print(list(result))
# [('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리')]

import itertools

result_longest = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result_longest))
# [('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]

## itertools.permutations
# itertools.permutations(iterable, r)은 반복 가능 객체 중에서 r개를 선택한 순열을 iterator로 반환하는 함수이다.
'''
1, 2, 3이라는 숫자가 적힌 3장의 카드에서 2장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하려면 어떻게 해야 할까?
[1,2,3]이라는 3장의 카드 중 순서에 상관없이 2장을 뽑는 경우의 수는 3가지이다.
- 1, 2
- 2, 3
- 1, 3
하지만 2자리 숫자이므로 3가지에 순서를 더해 6가지가 된다(순열)
- 1, 2
- 2, 1
- 2, 3
- 3, 2
- 1, 3
- 3, 1
'''

import itertools

print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# 따라서 만들 수 있는 2자리 숫자는 총 6가지다.
for a, b in itertools.permutations([1, 2, 3], 2):
    print(str(a) + str(b))
# 12
# 13
# 21
# 23
# 31
# 32

## itertools.combinations()
# 순서에 상관 없이 2장을 고르는 함수이다.
# 위의 예로는 총 3가지이다.
print(list(itertools.combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

'''
로또는 1 ~ 45 까지의 숫자 중 6개를 뽑는다.
총 나올 수 있는 경우의 수를 구하려면 어떻게 해야할까?
순서는 상관 없으므로 itertools.combinations() 를 사용하면 된다.
'''
result = list(itertools.combinations(range(1, 46), 6))
print(len(result))
# 8145060
# 로또 번호의 총 경우의 수는 8,145,060이다...

'''
중복 조합을 허용하는 경우는 어떻게 할까?
예를 들어 [1,2,3,4,5,5]와 같이 같은 수가 2번 이상 나와도 되는 경우의 수 말이다.
이런 경우 itertools.combinations_with_replacement()를 사용하면 된다.
'''
result = list(itertools.combinations_with_replacement(range(1, 46), 6))
print(len(result))


# 15890700
# 총 경우의 수는 15,890,700

## functools.reduce
# functools.reduce(function, iterable)은
# 함수를 반복 가능한 객체(iterable)의 요소에 차례대로 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수이다.

def add(data: list[int]):
    result = 0
    for i in data:
        result += i
    return result


data = [1, 2, 3, 4, 5]
result = add(data)
print(result)  # 15

# 이를 functools.reduce를 사용하면...

# reduce_test.py
import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)  # 15
# ((((1+2)+3)+4)+5)을 계산한다.

# functools.reduce()로 최대값을 구할수도 있다.
data = [1, 2, 3, 4, 10, 6, 7, 8, 9, 5]
result = functools.reduce(lambda x, y: x if x > y else y, data)
print(result)  # 10

## operator.itemgetter
# operator.itemgetter는 주로 sorted와 같은 함수의 key 매개변수에 적용하여
# 다양한 기준으로 정렬할 수 있도록 도와주는 모듈이다.
students = [
    ('jain', 22, 'A'),
    ('dave', 32, 'B'),
    ('sally', 17, 'B')
]

'''나이 순으로 정렬한다면?'''
# itemgetter1.py
from operator import itemgetter

students = [
    ('jain', 22, 'A'),
    ('dave', 32, 'B'),
    ('sally', 17, 'B')
]

result = sorted(students, key=itemgetter(1))
print(result)
# [('sally', 17, 'B'), ('jain', 22, 'A'), ('dave', 32, 'B')]
# itemgetter(1)은 students의 두 번째 요소를 기준으로 정렬하겠다는 의미이다.
# 즉, itemgetter(2)는 성적순으로 정렬한다.

# 이번엔 딕셔너리인 경우를 생각해보자.
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
# 이번엔 인덱스 번호가 아닌 key값을 인수로 넣어주면 된다.
result = sorted(students, key=itemgetter('age'))
print(result)
# [
#   {'name': 'sally', 'age': 17, 'grade': 'B'},
#   {'name': 'jane', 'age': 22, 'grade': 'A'},
#   {'name': 'dave', 'age': 32, 'grade': 'B'}
# ]

## operator.attrgetter()
# students 리스트의 요소가 튜플이 아닌 Student 클래스의 객체라면 attrgetter()를 사용해야 한다.

# attrgetter1.py
from operator import attrgetter


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f'Student({self.name}, {self.age}, {self.grade})'

    def __repr__(self):
        return f'Student({self.name}, {self.age}, {self.grade})'


students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]
result = sorted(students, key=attrgetter('age'))
print(result)
# [
#   Student(sally, 17, B),
#   Student(jane, 22, A),
#   Student(dave, 32, B)
# ]

## shutil
# shutil은 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈이다.
'''
작업 중인 파일을 자동으로 백업하는 기능을 구현하고자 
a.txt를 temp/a.txt.bak이라는 이름으로 복사하는 프로그램을 만들고자 한다.
a.txt 파일은 만드는 중이며, 백업용 temp 디렉토리는 이미 만들어졌다고 가정한다.
'''
# shutil_copy.py
import shutil

shutil.copyfile('a.txt', 'temp/a.txt.bak')

# move
# shutil.move('a.txt', 'temp/a.txt')

## glob
# 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면
# 특정 디렉토리에 있는 파일 이름 모두를 알아야 할 때가 있다.
# 이럴 때 glob을 사용한다.

# glob 모듈은 디렉토리 안의 파일들을 읽어서 반환한다.
# *, ? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수 있다.
# 다음은 현재 디렉토리의 파일 중 py로 끝나는 파일을 모두 찾아서 읽어들이는 예이다.
import glob

print(glob.glob('*.py'))
# ['built_in_function.py', 'class.py', 'exception.py', 'library.py', 'mod1.py', 'mod2.py', 'module.py', 'package.py']

## pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle의 dump 함수를 사용하여 딕셔너리 객체 data를 있는 그대로 저장하는 방법이다.
import pickle

f = open('test.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

# 불러오기
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)  # {1: 'python', 2: 'you need'}
f.close()

## os
# os 모듈은 환경 변수나 디렉토리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

# os.environ
# os.environ은 현재 시스템의 환경 변수값을 반환한다.
import os

print(os.environ)
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'AMDRMSDKPATH': 'C:\\Program Files\\AMD\\RyzenMasterSDK\\', 'APPDATA': 'C:\\Users\\bluea\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'OGOO_PC', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EFC_12564_1262719628': '1', 'EFC_12564_1592913036': '1', 'EFC_12564_2283032206': '1', 'EFC_12564_2775293581': '1', 'EFC_12564_3789132940': '1', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\bluea', 'LOCALAPPDATA': 'C:\\Users\\bluea\\AppData\\Local', 'LOGONSERVER': '\\\\OGOO_PC', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\bluea\\OneDrive', 'ONLINESERVICES': 'Online Services', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\bluea\\Documents\\develope\\python\\jump_to_python\\.venv\\Scripts;C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\HP\\HP One Agent;C:\\Program Files\\Bandizip\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\PuTTY\\;C:\\Program Files\\Git\\cmd;C:\\Users\\bluea\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\;C:\\Users\\bluea\\AppData\\Local\\Programs\\Python\\Python313\\;C:\\Users\\bluea\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\bluea\\AppData\\Local\\Programs\\Microsoft VS Code\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PLATFORMCODE': '1M', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD', 'PROCESSOR_LEVEL': '25', 'PROCESSOR_REVISION': '5000', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(.venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYCHARM_INTERACTIVE_PLOTS': '1', 'PYCHARM_PROJECT_ID': 'bb961299', 'PYCHARM_UUID': 'a18817a3-b336-3bc1-a7a1-b6eb83048646', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\bluea\\Documents\\develope\\python\\jump_to_python;C:/Program Files/JetBrains/PyCharm 2025.2.4/plugins/python-ce/helpers/pycharm_plotly_backend;C:/Program Files/JetBrains/PyCharm 2025.2.4/plugins/python-ce/helpers/pycharm_altair_backend;C:/Program Files/JetBrains/PyCharm 2025.2.4/plugins/python-ce/helpers/pycharm_matplotlib_backend;C:/Program Files/JetBrains/PyCharm 2025.2.4/plugins/python-ce/helpers/pycharm_display', 'PYTHONUNBUFFERED': '1', 'REGIONCODE': 'APJ', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\bluea\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\bluea\\AppData\\Local\\Temp', 'USERDOMAIN': 'OGOO_PC', 'USERDOMAIN_ROAMINGPROFILE': 'OGOO_PC', 'USERNAME': 'bluea', 'USERPROFILE': 'C:\\Users\\bluea', 'VBOX_HWVIRTEX_IGNORE_SVM_IN_USE': '1', 'VIRTUAL_ENV': 'C:\\Users\\bluea\\Documents\\develope\\python\\jump_to_python\\.venv', 'WINDIR': 'C:\\WINDOWS', '_OLD_VIRTUAL_PATH': 'C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\HP\\HP One Agent;C:\\Program Files\\Bandizip\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\PuTTY\\;C:\\Program Files\\Git\\cmd;C:\\Users\\bluea\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\;C:\\Users\\bluea\\AppData\\Local\\Programs\\Python\\Python313\\;C:\\Users\\bluea\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\bluea\\AppData\\Local\\Programs\\Microsoft VS Code\\bin', '_OLD_VIRTUAL_PROMPT': '$P$G'})
print(os.environ['PATH'])
# C:\Users\bluea\Documents\develope\python\jump_to_python\.venv\Scripts;C:\windows\system32;C:\windows;C:\windows\System32\Wbem;C:\windows\System32\WindowsPowerShell\v1.0\;C:\windows\System32\OpenSSH\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\HP\HP One Agent;C:\Program Files\Bandizip\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\PuTTY\;C:\Program Files\Git\cmd;C:\Users\bluea\AppData\Local\Programs\Python\Python313\Scripts\;C:\Users\bluea\AppData\Local\Programs\Python\Python313\;C:\Users\bluea\AppData\Local\Microsoft\WindowsApps;C:\Users\bluea\AppData\Local\Programs\Microsoft VS Code\bin

# os.chdir
# os.chdir을 사용하면 다음과 같이 현재 디렉토리의 위치를 변경할 수 있다.
print(os.getcwd())  # C:\Users\bluea\Documents\develope\python\jump_to_python\ch5
os.chdir("C:/windows")

# os.getcwd
# os.getcwd는 현재 자신의 디렉토리 위치를 반환한다.
print(os.getcwd())  # C:/windows

# os.system
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다.
# os.system("명령어")처럼 사용한다.
os.system('dir')
'''
 C ����̺��� ����: Windows
 ���� �Ϸ� ��ȣ: 2473-78C5

 C:\\Windows ���͸�

2025-11-03  ���� 06:50    <DIR>          .
2025-08-08  ���� 09:26    <DIR>          addins
...
'''

# os.popen
# os.popen은 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 반환한다.
f = os.popen('dir')
print(f.read())
f.close()
'''
 C 드라이브의 볼륨: Windows
 볼륨 일련 번호: 2473-78C5

 C:\\Windows 디렉터리

2025-11-03  오후 06:50    <DIR>          .
2025-08-08  오후 09:26    <DIR>          addins
'''

# 이 밖에 유용한 os 관련 함수는 다음과 같다.
'''
함수                  설명
os.mkdir(디렉토리)     디렉토리를 생성한다.
os.rmdir(디렉토리)     디렉토리를 삭제한다. 단, 디렉토리가 비어 있어야 삭제할 수 있다.
os.remove(파일)       파일을 지운다.
os.rename(src, dst)  src라는 이름의 파일을 dest라는 이름으로 변경한다.
'''

os.chdir('C:/Users/bluea/Documents/develope/python/jump_to_python/ch5')

## zipfile
# zipfile은 여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 때 사용하는 모듈이다.
'''
다음과 같은 3개의 텍스트 파일이 있다고 가정해보자.
zipfile/a.txt
zipfile/b.txt
zipfile/c.txt

이 3개의 파일을 하나로 합쳐 mytest.zip이라는 파일을 만들고,
이 파일을 다시 원래 텍스트 파일 3개로 해제하는 프로그램을 만드려면 어떻게 해야할까?
'''
# zipfile_test.py
import zipfile

# 파일 합치기
# with zipfile.ZipFile('zipfile_test/mytest.zip', 'w') as myzip:
#     myzip.write('zipfile_test/a.txt')
#     myzip.write('zipfile_test/b.txt')
#     myzip.write('zipfile_test/c.txt')

# 모두 해제
with zipfile.ZipFile('zipfile_test/mytest.zip', 'r') as myzip:
    myzip.extractall()

# 일부 해제
with zipfile.ZipFile('zipfile_test/mytest.zip', 'r') as myzip:
    myzip.extract('zipfile_test/a.txt')

# 파일을 압하는 경우 compression, compresslevel 옵션을 사용하면 된다.
with zipfile.ZipFile('zipfile_test/compress.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
    myzip.write('zipfile_test/compress.txt')
'''
compression에는 4가지 종류가 있다.
ZIP_STORED      압축하지 않고 파일을 zip으로만 묶는다. 속도가 빠름.
ZIP_DEFLATED    일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다. 호환성이 좋음.
ZIP_BZIP2       bzip2 압축으로 압축률이 높고 속도가 느리다.
ZIP_LZMA        lzma 압축으로 압축률이 높고 속도가 느리다. 7zip과 동일한 알고리즘으로 알려져 있다.

compressionlevel은 압축 수준을 의미하는 숫자값으로 1 ~ 9를 사용한다.
1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도는 가장 느리지만 압축률이 높다. 
'''

## threading
# 여러 스레드(thread)를 사용할 수 있게 해주는 모듈이다.

# thread_test.py
import time


def long_task():
    for i in range(5):
        time.sleep(0.1)
        print('working:%s' % i)


print('Start')
for i in range(5):
    long_task()

print('End')

# sleep이 1초이므로 5초 * 5번 = 25초의 시간이 걸린다.
# 스레드가 1개이기 때문에 순차적으로 실행되는 것을 확인할 수 있다.

# 스레드를 사용하면 long_task 함수를 동시에 실행할 수 있다.
import time
import threading


def long_task():
    for i in range(5):
        time.sleep(0.1)
        print('working:%s' % i)


print('Start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

# print('End')
# 25초 걸리던 작업이 5초 정도에 수행된다.
# 하지만 "Start"와 "End"가 먼저 출력되고 스레드의 결과가 출력된다.
# 이를 해결하기 위해선 다음과 같이 수정해주어야 한다.
for t in threads:
    t.join()

print('End')
# join으로 스레드가 종료될때까지 기다린다.
# 이제 End가 마지막에 출력된다.

## tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈이다.
# tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 반환한다.
import tempfile

filename = tempfile.mkstemp()
print(filename)
# (3, 'C:\\Users\\bluea\\AppData\\Local\\Temp\\tmpihsx94w1')

# tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 반환한다.
# 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.
# f.close()가 호출되면 이 파일은 자동 삭제된다.
import tempfile

f = tempfile.TemporaryFile()
f.close()


## traceback
# traceback은 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용한다.

# traceback_test.py
def a():
    return 1 / 0


def b():
    a()


def main():
    try:
        b()
    except:
        print('오류가 발생했습니다.')


main()
# 오류가 발생했습니다.
# 위와 같은 예일 때 어디서 어떤 오류가 발생했는지 추적하기가 어렵다.
# 이런 경우 traceback 모듈을 적용하면 된다.

# traceback_test.py
import traceback


def a():
    return 1 / 0


def b():
    a()


def main():
    try:
        b()
    except:
        print('오류가 발생했습니다.')
        print(traceback.format_exc())


main()
'''
오류가 발생했습니다.
Traceback (most recent call last):
  File "C:\\Users\\bluea\\Documents\\develope\\python\\jump_to_python\\ch5\\library.py", line 641, in main
    def main():
            ^^^
  File "C:\\Users\\bluea\\Documents\\develope\\python\\jump_to_python\\ch5\\library.py", line 636, in b
  File "C:\\Users\\bluea\\Documents\\develope\\python\\jump_to_python\\ch5\\library.py", line 632, in a
ZeroDivisionError: division by zero
'''
# 이제 오류를 추적할 수 있게 되었다.

## json
# json은 JSON 데이터를 쉽게 처리하고자 사용하는 모듈이다.

'''
다음은 myinfo.json 파일이다.
{
    "name": "홍길동",
    "birth": "0525",
    "age": 30
}
'''

# JSON 파일을 읽어 딕셔너리로 변환하려면 다음처럼 json 모듈을 사용하면 된다.
import json

with open('myinfo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(type(data))  # <class 'dict'>
print(data)
# {'name': '홍길동', 'birth': '0525', 'age': 30}

# JSON 파일을 읽을 때는 이 예처럼 json.load(파일 객체)를 사용한다.
# load() 함수는 읽은 데이터를 딕셔너리 자료형을 반환한다.
# 이와 반대로 자료형을 JSON 파일로 생성할 떄는 다음처럼 json.dump(딕셔너리, 파일_객체)를 사용한다.
import json

data = {'name': '홍길동', 'birth': '0525', 'age': 30, 'location': 'seoul'}
with open('myinfo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

# 이번에는 JSON 문자열로 만드는 방법에 대해 알아보자.
import json

d = {"name": "\ud64d\uae38\ub3d9", "birth": "0525", "age": 30, "location": "seoul"}
json_data = json.dumps(d)
print(json_data)
# {"name": "\ud64d\uae38\ub3d9", "birth": "0525", "age": 30, "location": "seoul"}
'''
위와 같이 json.dump나 json.dumps를 사용하게 되면 한글이 유니코드로 치환된다.
이는 역변환시 다시 치환되기 때문에 문제가 발생하지 않는다.
'''
# 다시 역변환 하려면 json.loads() 함수를 사용한다.
print(json.loads(json_data))
# {'name': '홍길동', 'birth': '0525', 'age': 30, 'location': 'seoul'}
# 잘 변환되는 것을 확인할 수 있다.

# 유니 코드로 변경되는 것을 방지하는 방법도 있다.
# ensure_ascii=False 옵션을 사용하는 것이다.
d = {"name": "\ud64d\uae38\ub3d9", "birth": "0525", "age": 30, "location": "seoul"}
json_data = json.dumps(d, ensure_ascii=False)
print(json_data)
# {'name': '홍길동', 'birth': '0525', 'age': 30, 'location': 'seoul'}
print(json.loads(json_data))
# {"name": "홍길동", "birth": "0525", "age": 30, "location": "seoul"}

# 출력되는 JSON 문자열을 보기 좋게 정렬하려면 indent 옵션을 추가하면 된다.
print(json.dumps(d, ensure_ascii=False, indent=2))
{
    "name": "홍길동",
    "birth": "0525",
    "age": 30,
    "location": "seoul"
}

# 딕셔너리 외에 리스트나 튜플처럼 다른 자료형도 JSON 문자열로 변경할 수 있다.
print(json.dumps([1, 2, 3]))
# [1, 2, 3]
print(json.dumps((4, 5, 6)))
# [4, 5, 6]

## urllib
# urllib은 URL을 읽고 분석할 때 사용하는 모듈이다.

# 브라우저로 위키독스의 특정 페이지를 읽으려면 다음과 같이 요청하면 된다.
'''
https://wikidocs.net/페이지_번호 (예: https://wikidocs.net/12)
'''
# 그러면 오프라인으로도 읽을 수 있도록
# 특정 페이지를 wikidocs_페이지번호.html 파일로 저장하는 함수는 어떻게 만들어야 할까?
# URL을 호출하여 원하는 리소스를 얻으려면 urllib 모듈을 사용해야 한다.

# utllib_test.py
import urllib.request


def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as res:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(res.read())


get_wikidocs(33)

# get_wikidocs(page)는 위키독스의 페이지 번호를 입력받아
# 해당 페이지의 리소스 내용을 파일로 저장하는 함수이다.
# urllib.request.urlopen(resource)로 res 객체를 생성하고,
# res.read()로 리소스 내용 전체를 읽어 이를 저장할 수 있다.
# 예를 들어 get_wikidocs(12)라고 호출하면 https://wikidocs.net/12 웹페이지를 wikidocs_12.html라는 파일로 저장한다.

## webbrowser
# webbrowser는 파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용하는 모듈이다.

# webbrowser_test.py
import webbrowser

# 이미 열린 브라우저
webbrowser.open('https://python.org')

# 새로운 브라우저
webbrowser.open_new('http://python.org')
