### class.py

## Why are classes necessary?
# 프로그래머들이 가장 많이 사용하는 언어 중 하나인 C에는 클래스가 없다.
# 이 말은 곧, 클래스 없이도 프로그램을 충분히 만들 수 있다는 뜻이다.
# 파이썬으로 만든 프로그램을 봐도 클래스를 사용하지 않고 만드는 경우도 많다.
# 따라서, 클래스는 꼭 필요한 요소는 아니다.
# 하지만 프로그램을 작성할 때 클래스를 적재적소에 사용하면 이익이 많다.

## Calculator
# 계산기는 이전에 계산한 결과값을 기억하고 있어야 한다.

# 만약 함수로 구현한다면 어떤 형식일까?
result = 0


def add(num: int):
    global result
    result += num
    return result


print(add(3))  # 3
print(add(4))  # 7

# 그런데 만약 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야 할까?
# 각 계산기는 각각의 결과값을 유지해야 하므로 위와 같이 add 함수 하나만으로는 결과값을 따로 유지할 수 없다.
result1 = 0
result2 = 0


def add1(num: int):  # 계산기1
    global result1
    result1 += num
    return result1


def add2(num: int):  # 계산기2
    global result2
    result2 += num
    return result2


print(add1(3))  # 3
print(add1(4))  # 7
print(add2(3))  # 3
print(add2(7))  # 10


# 계산기 1의 결과값이 계산기 2에 아무런 영향을 끼치지 않는 것을 확인할 수 있다.
# 하지만 계산기가 점차 많이 필요해진다면 상황은 점점 어려워질 것이다.

# 이런 경우 클래스를 사용하면 다음과 같이 간단하게 해결할 수 있다.
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num: int):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))  # 3
print(cal1.add(4))  # 7
print(cal2.add(3))  # 3
print(cal2.add(7))  # 10


# Calculator 클래스로 만든 별개의 계산기 cal1, cal2(객체라고 부른다)가 각각의 역할을 수행한다.
# 계산기의 결과값 역시 독립적인 값이 유지된다.
# 클래스를 사용하면 계산기 대수가 늘어나도 객체를 생성하면 되므로 함수만 사용할 때마다 간단하게 프로그램을 작성할 수 있다.

# 빼기 기능을 더해보자.
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num: int):
        self.result += num
        return self.result

    def minus(self, num: int):
        self.result -= num
        return self.result


## class and object
# 클래스로 만든 객체에는 중요한 특징이 있다.
# 객체마다 고유한 성격을 가진다는 것이다.
# 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

# 다음은 파이썬 클래스의 가장 간단한 예이다.
class Cookie:
    pass


# Cookie 클래스는 아무런 기능도 가지고 있지 않은 껍질뿐인 클래스이다.
# 하지만 껍질뿐인 클래스도 객체를 생성할 수 있다.
a = Cookie()
b = Cookie()

# 클래스로 만든 객체를 '인스턴스'라고도 한다.
a = Cookie()


# 여기서 a는 객체이다.
# 그리고 a 객체는 Cookie의 인스턴스이다.
# 즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.


## Creating a class for arithmetic operations
# 사칙 연산을 수행하는 클래스를 직접 만들며 배워 보자.

# 클래스를 만들기 전 다음처럼 동작한다고 가정해보자.
# 1. a = FourCal()을 입력해서 a라는 객체를 만든다.
# 2. a.setdata(4, 2)처럼 입력해서 숫자 4와 2를 a에 지정해 준다.
# 3. a.add()를 수행하면 두 수를 합한 결과(4 + 2)를 리턴한다.
# 4. a.mul()를 수행하면 두 수를 곱한 결과(4 * 2)를 리턴한다.
# 5. a.sub()를 수행하면 두 수를 뺀 결과(4 - 2)를 리턴한다.
# 6. a.div()를 수행하면 두 수를 나눈 결과(4 / 2)를 리턴한다.

## Creating class structure
class FourCal:
    pass


# 위와 같이 클래스를 간단하게 만들 수 있따.
# pass는 아무것도 수행하지 않는 문법으로, 임시로 코드를 작성할 때 주로 사용한다.
a = FourCal()
print(type(a))  # <class '__main__.FourCal'>

# type은 파이썬의 내장 함수로, 객체의 타입을 출력한다.

## Specifying a number to operate on a object
# 하지만 생성한 객체 a는 아무런 기능도 하지 못한다.
# 연산을 수행할 두 숫자(4, 2)를 지정할 수 있도록 만들어보자.
'''
a.setdata(4,2)
'''


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


# 이제 setdata 함수를 정의했다.
# 클래스 안에 구현한 함수는 다른 말로 메서드(method)라고 부른다.

# parameter of setdata method
# setdata 메서드는 매개변수로 self,first, second 3개의 입력값을 받는다.
# 근데 일반 함수와 달리 첫 번째 매개변수 self는 특별한 의미를 가진다.
# 다음과 같이 a 객체를 만들고 a 객체를 통해 setdata 메서드를 호출해 보자.
a = FourCal()
a.setdata(4, 2)
# self는 생략된 first, second 매개변수만 전달되는 것을 볼 수 있다.
# 이는 setdata 메서드의 첫 번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달하기 떄문이다.
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.

# 메서드를 호출하는 또 다른 방법(잘 사용하진 않음)
a = FourCal()
FourCal.setdata(a, 4, 2)


# 이제 setdata 메서드의 수행문에 대해 알아보자.
def setdata(self, first, second):
    self.first = first
    self.second = second


# a.setdata(4,2)처럼 호출하면
# setdata 메서드의 매개변수 first, second에 각각 4, 2 값이 전달된다.
# self.first = 4
# self.second = 2
# self는 a 객체이므로 다음과 같이 해석할 수 있다.
# a.first = 4
# a.second = 2
a = FourCal()
a.setdata(4, 2)
print(a.first)  # 4
print(a.second)  # 2

# 이번에는 다음과 같이 a, b 객체를 만들어보자.
a = FourCal()
b = FourCal()

# 그리고 a 객체의 객체변수 first를 다음과 같이 생성한다.
a.setdata(4, 2)
print(a.first)  # 4

# 이번에는 b 객체의 객체변수 first를 다음과 같이 생성한다.
b.setdata(3, 7)
print(b.first)  # 3
print(a.first)  # 4
# 각 객체는 독립적인 객체변수를 가지는 것을 확인할 수 있다.

## Create a plus method
# 이제 2개의 숫자를 더하는 기능을 만들어보자.
'''
a = FourCal()
a.setdata(4, 2)
a.add()
'''


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second


a = FourCal()
a.setdata(4, 2)
print(a.add())  # 6


## Create other method
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second


a = FourCal()
a.setdata(4, 2)
b = FourCal()
b.setdata(3, 8)
print(a.add())  # 6
print(a.mul())  # 8
print(a.sub())  # 2
print(a.div())  # 2
print(b.add())  # 11
print(b.mul())  # 24
print(b.sub())  # -5
print(b.div())  # 0.375


## contructor
# 이번에는 우리가 만든 FourCal 클래스를 다음과 같이 사용해보자.
# a = FourCal()
# a.add()


# return self.first + self.second
#        ^^^^^^^^^^
# AttributeError: 'FourCal' object has no attribute 'first

# setdata 메서드를 수행하지 않고(first, second를 초기화하지 않고) 바로 연산을 하였기 때문에 에러가 발생하는 것이다.

# 이런 경우 생성자(contructor)를 사용하면 된다.

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second


# 생성자는 __init__으로 선언해주면 되며, 객체가 생성되는 시점에 자동으로 호출된다.
# a = FourCal()
#    a = FourCal()
# TypeError: FourCal.__init__() missing 2 required positional arguments: 'first' and 'second'

# 이제 a 객체를 만들 때 에러가 발생하는 것을 볼 수 있다.
# 에러의 내용은 객체 생성시 first와 second

a = FourCal(4, 2)
# 이제 위와 같이 객체를 생성해 주어야 한다.
print(a.add())  # 6
print(a.mul())  # 8


## class inheritance
# 상속(inheritance)이란 '물려받다'라는 뜻으로 클래스에도 이 개념을 적용할 수 있다.
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
# 상속 기능을 사용하여 a^b값을 구할 수 있는 기능을 추가해보자.
class MoreFourCal(FourCal):
    pass


# 클래스를 상속하기 위해서 다음처럼 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
'''
class 클래스_이름(상속할_클래스_이름)
'''
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있다.
a = MoreFourCal(2, 3)
print(a.add())  # 5
print(a.mul())  # 6


# 상속받은 FourCal 클래스의 기능을 모두 사용할 수 있다는 것을 확인할 수 있다.

# 이제 원래 목적을 달성해보자
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second


a = MoreFourCal(4, 2)
print(a.pow())  # 16
print(a.add())  # 6


## Method overriding
# 이번에는 FourCal 클래스를 다음과 같이 실행해 보자.
# a = FourCal(4, 0)
# print(a.div())
#    return self.first / self.second
#           ~~~~~~~~~~~^~~~~~~~~~~~~
# ZeroDivisionError: division by zero
# 0으로 나눌 수 없다는 에러가 발생한다.
# 0으로 나눌 때 오류가 아닌 값 0을 리턴받고 싶다면 어떻게 해야 할까?
class safeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


# FourCal 클래스에 있는 div 메서드를 재정의했다.
# 이를 메서드 오버라이딩(method overriding)이라고 한다.
# 이렇게 오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
a = safeFourCal(4, 0)
print(a.div())  # 0


## Class variables
# 객체 변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지한다는 점을 알아보았다.
# 객체 변수와는 성격이 다른 클래스 변수에 대해 알아보자.
class Family:
    lastname = "김"


# Family 클래스에 선언한 lastname이 바로 클래스 변수이다.
# 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성한다.
print(Family.lastname)  # 김
a = Family()
b = Family()
print(a.lastname)  # 김
print(b.lastname)  # 김

# 만약 Family 클래스의 lastname을 "박"으로 변경하면 어떻게 될까?
Family.lastname = '박'
print(a.lastname)  # 박
print(b.lastname)  # 박

# 클래스 변수의 값을 변경했더니 클래스로 만든 모든 객체의 lastname 값도 모두 변경된다는 것을 확인할 수 있었다.
