### module.py
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든 파이썬 파일이라고도 할 수 있다.
# 다른 사람들이 미리 만들어 놓은 모듈을 사용할 수도 있고 우리가 직접 만들어 사용할 수도 있다.

## Creating module
# 간단한 모듈을 만들어보자.
# mod1.py 파일

## Importing module
# 만든 mod1.py 파일, 즉 모듈을 불러와 보자.
import mod1

print(mod1.add(3, 4))  # 7
print(mod1.sub(4, 2))  # 2

# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어이다.
'''
import 모듈_이름
'''
# 때로는 mod1.add처럼 쓰지 않고 add, sub처럼 사용하려면 다음과 같이 사용하면 된다.
from mod1 import add

print(add(3, 4))  # 7

# 그런데 이렇게 하면 add 함수만 사용할 수 있다.
# 모두 사용하려면 다음과 같이 사용하면 된다
from mod1 import add, sub

print(add(3, 4))  # 7
print(sub(3, 4))  # -1

# 혹은 * 문자를 사용한다.
# *는 모든 함수를 불러온다.
from mod1 import *

print(add(4, 4))  # 8
print(sub(3, 7))  # -4

## Meaning of if __name__ == "__main__":
# 이번에는 mod1.py 파일 하단에 다음을 추가해보자.
'''
print(add(1,4)) # 5
print(sub(4,2)) # 2
'''
# import mod1만 했을 뿐인데 mod1.py 파일의 print 부분이 출력되는 것을 확인할 수 있다.
# 이를 방지하기 위해선 if __name__ == '__main__": 을 사용하면 된다.
# 이는 해당 파일을 직접 수행해야 if 다음 문장이 수행된다.
# 즉, import mod1 같이 모듈을 불러 사용하는 환경에서는 실행되지 않는다.

## Modules containing classes, variables, etc.
# 지금까지 살펴본 모듈은 함수만 포함했지만, 클래스나 변수 등을 포함할 수도 있다.
# mod2.py
import mod2

print(mod2.PI)  # 3.141592
# PI 변수를 불러 올 수 있다.
print(mod2.add(mod2.PI, 4.4))  # 7.541592

# How to load a moudle from another directory
# 다른 디렉토리에서 모듈을 불러오는 방법
# sys 모듈을 통해 다른 디렉토리에서 모듈을 불러 올 수 있다.
import sys

print(sys.path)
# sys.path는 라이브러리가 설치되어 있는 디렉토리 목록을 표시해준다.
sys.path.append("C:/Users/bluea/Documents/develope/python/jump_to_python/ch5/other")
# sys.path.append를 통해 other.py가 있는 디렉토리를 추가해주었다.

import other

print(other.PI)  # 3.141592
# 이상 없이 모듈을 불러와서 사용할 수 있다.

## Using the PYTHONPATH envionment variable
# 모듈을 불러오는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 것이다.
'''
터미널에서 다음을 실행한다.
set PYTHONPATH=C:/Users/bluea/Documents/develope/python/jump_to_python/ch5/other
'''
import other

print(other.PI)  # 3.141592
# MAC이나 유닉스 환경에서는 set 대신 export 명령을 사용해야 한다.
