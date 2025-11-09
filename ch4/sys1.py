### program.py

## using sys module
# sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다.
# sys 모듈을 사용하려면 import sys를 상단에 써준다.
import sys

args = sys.argv[1:]
for i in args:
    print(i)

# python sys1.py aaa bbb ccc
# aaa
# bbb
# ccc
