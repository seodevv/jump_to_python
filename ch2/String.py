# String.py
a = "Hello World!"
b = 'Hello World!'
c = """Hello World!"""
d = '''Hello World!'''

print(a)
print(b)
print(c)
print(d)

quotes = "Python's favorite food is perl"
print(quotes)

spacing = "Life is too short\nYou need python"
spacing_other = '''Life is to short
You need python'''
print(spacing)
print(spacing_other)


print(len(a))

slicing = 'Life is too short, You need python'
print(slicing)
print(slicing[0:4])
print(slicing[19:])
print(slicing[:19])
print(slicing[:])
print(slicing[19:-7])
print(slicing[19:-15])

str = "20230331Rainy"
year = str[0:4]
month = str[4:6]
day = str[6:8]
wheather = str[8:]
print(year)
print(month)
print(day)
print(wheather)

wrong = 'pithon'
# wrong[1] = y  #this is error
print(wrong)
print(wrong[:1]+'y'+wrong[2:])

# formatting
print("I eat %d apples." %3)
print("I eat %s apples." %"five")

number = 3
print("I eat %d apples." %number)

number = 10
day = 'three'
print("I ate %d apples. so I was sick for %s days." %(number,day))

# print("Error is %d%" %3) # this is error
print("Error is %d%%" %3)
print("Error is %")

# spacing
print("%10s" %"hi")
print("%-10sjane." %"hi")
print("%0.4f" %3.42134234)

# formatting
print("I eat {0} apples.".format(3))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day))
print("I ate {number} apples. so I was sick for {day} days".format(number=10,day="five"))

# align
print("{0:<10}".format('hi')) # left
print("{0:>10}".format('hi')) # right
print("{0:^10}".format('hi')) # center

# fill
print("{0:!<10}".format('hi')) # !
print("{0:#>10}".format('hi')) # #
print("{0:@^10}".format('hi')) # @

# float expression
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{0:<10.4f}".format(y))
print("{0:!^10.4f}".format(y))

# and expression
print("{{ and }}".format())

# f string formatting
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f"나는 내년이면 {age + 1}살이 된다.")

d = {"name": "홍길동", "age": 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":!<10}')
print(f'{"hi":@>10}')
print(f'{"hi":=^10}')
print(f'{123 + 456:=^11}')
print(f'{y:0.4f}')
print(f'{y:=^10.4f}')

print(f'{{ and }}')

print(f'나는 {15000000:,}원이 필요해')

# function
a = 'hobby'
print(a.count('b'))

a = 'Python is the best choice'
print(a.find('b')) # found : 14
print(a.find('k')) # not found : -1

a = "Life is too short"
print(a.index('t')) # found : 8
# print(a.index('k')) # not found : error occured

str = ','
print(str.join('abcd')) # a,b,c,d,
print(str.join(['a','b','c','d'])) # a,b,c,d

print('hi'.upper()) # HI
print('HI'.lower()) # hi

a = ' hi '
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())

a = "Life is to short"
print(a.replace("Life", "Your leg"))

a = "Life is to short"
print(a.split())
b = 'a:b:c:d'
print(b.split(":"))

# isalpha
# 문자열이 알파벳으로만 구성되어 있는지 확인
s = "Python"
print(s.isalpha()) # True
s = "Python3"
print(s.isalpha()) # False
s = 'Hello World'
print(s.isalpha()) # False

# isdigit
# 문자열이 숫자(0~9)로만 구성되어 있는지 확인
s = '12345'
print(s.isdigit()) # True
s = '1234a'
print(s.isdigit()) # False
s = '12 34'
print(s.isdigit()) # False

# startswith
# 문자열이 특정 문자(열)로 시작하는지 확인
s = 'Life is too short'
print(s.startswith('Life')) # True
print(s.startswith('life')) # False

# endswith
# 문자열이 특정 문자(열)로 끝나는지 확인
s = "Life is too short"
print(s.endswith('short')) # True
print(s.endswith('too')) # False


