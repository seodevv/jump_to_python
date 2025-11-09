### package.py

# 파이썬에서 패키지(packages)란 관련 있는 모듈의 집합을 말한다.
# 패키지는 파이썬 모듈을 계층적(디렉토리 구조)으로 관리할 수 있게 해준다.
# 파이썬에서 모듈은 하나의 .py 파일이다.

# 파이썬의 패키지는 디렉토리와 파이썬 모듈로 이루어진다.
# 다음은 game이라는 패키지의 구조이다.
'''
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
'''
# game, sound, graphic, play는 디렉토리, 확장자가 .py인 파일은 파이썬 모듈이다.
# game 디렉토리가 이 패키지의 루트 디렉토리이며
# sound, graphic, play는 서브 디렉토리이다.

# 간단한 파이썬 프로그램이 아니라면
# 이렇게 패키지 구조로 프로그램을 만드는 것이 공동 작업이나 유지 보수 등 여러면에서 유리하다.
# 또한 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.

## Creating package
# game 패키지를 직접 만들어 보면서 패키지에 대해 알아보자.
# 1. game 및 기타 서브 디렉토리를 생성하고, 모듈을 만들어보자.
'''
game/__init__.py
game/sound/__init__.py
game/sound/echo.py
game/graphic/__init__.py
game/graphic/render.py
'''

# 2. echo.py 파일의 내용은 다음과 같이 작성한다.
'''
def echo_test():
    print('echo')
'''

# 3. render.py 파일의 내용은 다음과 같이 작성한다.
'''
def render_test():
    print('render')
'''

# 4. game 패키지를 참조할 수 있도록 PYTHONPATH 환경 변수에 디렉토리를 추가한다.
'''
set PYTHONPATH=C:/Users/bluea/Documents/develope/python/jump_to_python
'''

## Running functions within a package
# 이제 패키지를 사용하여 echo.py 파일의 echo_test 함수를 실행해보자.
# 함수를 실행하는 방법은 3가지가 있다.

# 첫 번째는 echo 모듈을 import하여 실행하는 방법이다.
'''
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
'''

# 두 번째는 echo 모듈이 있는 디렉토리까지 from ... import하여 실행하는 방법이다.
'''
>>> from game.sound import echo
>>> echo.echo_test()
echo
'''

# 세 번째는 echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법이다.
'''
>>> from game.sound.echo import echo_test
>>> echo_test()
echo
'''

# 하지만 다음과 같이 echo_test 함수를 사용하는 방법은 불가능하다.
'''
>>> import game
>>> game.sound.echo.echo_test()
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    game.sound.echo.echo_test()
    ^^^^^^^^^^
AttributeError: module 'game' has no attribute 'sound'
'''
# 에러가 발생한다.

'''
>>> import game.sound.echo.echo_test
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    import game.sound.echo.echo_test
ModuleNotFoundError: No module named 'game.sound.echo.echo_test'; 'game.sound.echo' is not a package
'''
# 항상 마지막은 모듈이어야 하기 떄문이 이 import 문은 에러가 발생한다.

## Purpose of __init__.py
# __init__.py 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다.
# 만약 game, sound, graphic 등 패키지에 포함된 디렉토리에 해당 파일이 없으면 패키지로 인식되지 않는다.
'''python 3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다.'''
# 또한 __init__.py 파일은 패키지와 관련된 설정이나 초기화 코드를 포함할 수 있다.

## Defining package variables and functions
# 패키지 수준에서 변수와 함수를 정의할 수 있다.
'''
# game/__init__.py
VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")
'''

# 이렇게 패키지의 __init__.py 파일에 정의된 변수와 함수는 다음과 같이 사용할 수 있다.
'''
>>> import game
>>> print(game.VERSION)
3.5
>>> game.print_version_info()
The version of this game is 3.5.
'''

## Pre-import modules within the package
# __init__.py 파일에 패키지 내의 다른 모듈을 미리 import하여 패키지를 사용하는 코드에서 간편하게 접근할 수 있다.
'''
# game/__init__.py
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")
'''

# 이제 패키지를 사용하는 코드에서는 다음과 같이 간편하게 game 패키지를 통해 render_test 함수를 사용할 수 있다.
'''
>>> import game
>>> game.render_test()
render
'''

## Package initialization
# __init__.py 파일에 패키지를 처음 불러올 때 실행되어야 하는 코드를 작성할 수 있다.
# 예를 들어, 데이터베이스 연결이나 설정 파일 로드와 같은 작업을 수행할 수 있다.
'''
# game/__init__.py
from .graphic.render import render_test

VERSION = 3.5


def print_version_info():
    print(f"The version of this game is {VERSION}.")


print("Initializing game ...")
'''

# 이렇게 하면 패키지를 처음 import 할 때 초기화 코드가 실행된다.

# game 패키지의 초기화 코드는 game 패키지의 하위 모듈의 함수를 import할 경우에도 실행된다.

## __all__
# 이번에는 다음을 따라 해 보자.
'''
>>> from game.sound import *
Initializing game ...
>>> echo.echo_test()
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    echo.echo_test()
    ^^^^
'''

# * 로 import할 때는 __init__.py 파일에 __all__ 변수를 설정해주어야 한다.
'''
# game/sound/__init__.py
__all__ = ['echo']
'''
# __all__이 의미하는 것은 sound 디렉토리에서 *를 사용하여 import할 경우,
# 이곳에 정의된 echo 모듈만 import된다는 의미이다.
'''
>>> from game.sound import *
Initializing game ...
>>> echo.echo_test()
echo
'''

## relative path package
# 만약 graphic 디렉토리의 render.py 모듈에서 sound 디렉토리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할까?
# 다음과 같이 render.py를 수정하면 가능하다.
'''
### game/graphic/render.py
from game.sound.echo import echo_test

def render_test():
    print('render')
    echo_test()
'''

'''
>>> from game.graphic.render import render_test
Initializing game ...
>>> render_test()
render
echo
'''
# 이상 없이 잘 수행된다.

# from game.sound.echo import echo_test를 입력해 전체 경로를 사용하여 import할 수도 있지만,
# 다음과 같이 상대경로로 import하는 것도 가능하다.
'''
from ..sound.echo import echo_test

def render_test():
    print('render')
    echo_test()
'''

'''
>>> from game.graphic.render import render_test
Initializing game ...
>>> render_test()
render
echo
'''
# 마찬가지로 이상 없이 잘 수행된다.
# 여기서 ..은 render.py 파일의 부모 디렉토리를 의미한다.
'''
접근자     설명
..        부모 디렉토리
.         현재 디렉토리
'''
