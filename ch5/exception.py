### exception.py
# 프로그램을 만들다 보면 수없이 많은 오류를 만나게 된다.
# 오류가 발생하는 이유는 프로그램이 잘못 동작하는 것을 막기 위한 배려이다.

## where does the error occur?
# 어떤 상황에서 오류가 발생하는지 한번 알아보자.

# 먼저 존재하지 않는 파일을 사용하려고 시도했을 때 밠갱하는 오류이다.
# f = open('없는파일', 'r')
'''
f = open('없는파일', 'r')
    ~~~~^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '없는파일'
'''
# 파일을 열려고 시도하면 FileNotFoundError 오류가 발생한다.

# 이번에는 0으로 다른 숫자를 나눠보자.
# 4 / 0
'''
    4 / 0
    ~~^~~
ZeroDivisionError: division by zero
'''
# ZeroDivisionError 오류가 발생한다.

# 마지막으로 빈번하게 일어나는 오류이다.
a = [1, 2, 3]
# a[3]
'''
    a[3]
    ~^^^
IndexError: list index out of range
'''
# a[3]은 a의 4 번째 요소값을 가리키는데, a 리스트에 존재하지 않는다.
# 따라서 IndexError 오류가 발생한다.

# 파이썬은 이러한 오류가 발생하면 프로그램을 중단하고 오류 메시지를 보여 준다.

## Error Exception handling techniques

# try-except statement
# 다음은 오류를 처리하기 위한 try-except 문의 기본 구조이다.
'''
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
'''
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
# 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

'''
except [발생오류 [as 오류변수]]:
'''
# 위 구문을 보면 []를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례적인 표기법이다.
# 즉, except 구문은 다음 3가지 방법으로 사용할 수 있다.

# 1.try-except만 쓰는 방법
'''
try:
    ...
except:
    ...
'''
# 이 경우에는 오류의 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

# 2.발생 오류만 포함한 except 문
'''
try:
    ...
except 발생오류:
    ...
'''
# 이 경우는 오류가 발생했을 때
# except 문에 미리 정해 놓은 오류와 동일한 오류일 경우에만 except 블록을 수행할 수 있다.

# 3. 발생 오류와 오류 변수까지 포함한 except 문
'''
try:
    ...
except 발생오류 as 오류변수:
    ...
'''
# 이 경우는 두 번째 경우에서 오류의 내용까지 알고 싶을 때 사용한다.

# try_except.py
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)  # division by zero
# ZeroDivisionError가 발생하여 except 블록이 실행되고
# 오류 변수 e에 담기는 오류 메시지를 출력할 수 있다.

## try-finally 문
# try 문에는 finally 절을 사용할 수 있다.
# finally 절은 tryt 문 수행 도중 예외 발생 여부와 상관 없이 항상 수행된다.
# 보통 finally 절은 사용한 리소스를 close해야 할 때 많이 사용한다.

# try_finally.py
try:
    f = open('foo.txt', 'w', encoding='utf-8')
    # 무언가를 수행한다.
finally:
    f.close()
# foo.txt 파일을 쓰기 모드로 연 후 예외 발생 여부에 상관없이 항상 파일을 닫아 준다.

## Handling multiple errors
# try 문 안에서 여러 개의 오류를 처리하려면 다음과 같이 사용해야 한다.
'''
try:
    ...
except 발생오류1:
    ...
except 발생오류2:
    ...
'''

# 즉, 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다.

# many_error.py
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print("인덱싱 할 수 없습니다.")

# 인덱싱 할 수 없습니다.
# 인덱싱 오류가 먼저 발생했으므로 ZeroDivisionError 오류는 발생하지 않는다.

# 앞에서 알아본 바와 같이 오류 메시지도 같이 확인할 수 있다.
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
# list index out of range

# 에러를 한번에 묶어서 처리할 수도 있다.
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)

## try-else statement
# try 문에는 else 절을 사용할 수도 있다.
'''
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
else: # 오류가 없을 경우에만 실행
    ...
'''
# 오류가 발생하지 않을 경우에만 else 절이 실행된다.

# try_else.py
try:
    age = int(input('나이를 입력하세요: '))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print("환영합니다.")
# 숫자를 입력할 경우 else 절이 수행된다.
# 숫자가 아닌 값을 입력하면 except 절이 수행된다.


## Avoid errors
# 코드를 작성하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있다.
# 예를 들어, 여러 파일을 처리하는 중에 일부 파일이 없더라도 프로그램을 계속 실행하고 싶을 때가 있다.

# process_scores.py
students = ['김철수', '이영희', '박민수', '최유진']

for student in students:
    try:
        with open(f'{student}_성적.txt', 'r') as f:
            score = f.read()
            print(f'{student}의 성적: {score}')
    except FileNotFoundError:
        print(f'{student}의 성적 파일이 없습니다. 건너뜁니다.')
        continue
# 위 코드에서 일부 학생의 성적 파일이 없더라도 프로그램이 중단되지 않는다.

# 때로는 오류를 완전 무시하고 싶을 때도 있다.
# 이럴 땐 pass를 사용한다.

# error_pass.py
try:
    # 설정 파일을 읽으려 시도
    f = open('설정파일.txt', 'r')
    config = f.read()
    f.close()
except FileNotFoundError:
    pass

# 프로그램의 주요 기능은 계속 수행
print('프로그램이 정상적으로 실행됩니다.')


## Intentionally causing errors
# 종종 오류를 일부러 발생시켜야 할 경우도 생긴다.
# raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.

# 예를 들어
# Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우가 있을 수 있다.

# error_raise.py
class Bird:
    def fly(self):
        raise NotImplementedError


# Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여준다.from
# 만약 자식 클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출하면 어떻게 될까?
'''NotImplementedError는 파이썬에 정의된 오류로, 꼭 작성해야 하는 부분을 구현하지 않았을 때 오류가 발생한다.'''


class Eagle(Bird):
    pass


# eagle = Eagle()
# eagle.fly()
'''
    eagle.fly()
    ~~~~~~~~~^^
  File "C:\\Users\\bluea\\Documents\\dev\\python\\jump_to_python\\ch5\\exception.py", line 221, in fly
    raise NotImplementedError
NotImplementedError
'''


# fly 메서드를 오버라이딩으로 구현하지 않았기 때문에 오류가 발생한다.

# NotImplementedError가 발생하지 않게 하려면 fly 메서드를 오버라이딩 해야한다.
class Eagle(Bird):
    def fly(self):
        print('very fast')


eagle = Eagle()
eagle.fly()


# very fast
# 이제 오류가 발생하지 않는다.

## Creating exception
# 프로그램을 수행하다가 특수한 경우에만 예외 처리를 하려고 종종 예외를 만들어서 사용한다.
# Exception 클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    pass


# 그리고 별명을 출력하는 함수를 작성해 보자.
def say_nick(nick: str):
    if nick == '바보':
        raise MyError()
    print(nick)


say_nick('천사')
# say_nick('바보')
'''
    say_nick('바보')
    ~~~~~~~~^^^^^^^^
  File "C:\\Users\\bluea\\Documents\\develope\\python\\jump_to_python\\ch5\\exception.py", line 269, in say_nick
    raise MyError()
MyError
'''
# "바보"는 MyError가 발생하는 것을 볼 수 있다.

# 이번에는 예외 처리 기법을 사용하여 MyError 발생을 예외 처리해 보자.
try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print("허용하지 않은 별명입니다.")
# 천사
# 허용하지 않은 별명입니다.

# 오류 메시지를 사용하고 싶다면 다음과 같이 하면 된다.
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)


# 하지만 실행해 보면 print(e) 오류 메시지가 출력되지 않는다.
# MyError 클래스는 __str__ 메서드를 구현하지 않았기 때문이다.
class MyError(Exception):
    def __str__(self):
        return '허용하지 않은 별명입니다.'


try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
# 천사
# 허용하지 않은 별명입니다.
# 이제 메시지가 잘 출력된다.
