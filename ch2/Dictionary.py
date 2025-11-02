### Dictionary.py
# 키(key)와 값(value) 형태로 이루어진 자료형
# 연관 배열(associative array) 또는 해시(hash)라고도 함
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a = {1: 'hi'}
a = {'a': [1, 2, 3]}

## insert
a = {1: 'a'}
a[2] = 'b'
print(a)  # {1: 'a', 2: 'b'}
a['name'] = 'pey'
print(a)  # {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1, 2, 3]
print(a)  # {1: 'a', 2: 'b', 'name': 'pey', 3: [1,2,3]}

## delete
del a[1]
print(a)  # {2: 'b', 'name': 'pey', 3: [1,2,3]}

## usage
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])  # 10
print(grade['julliet'])  # 99

## example
a = {1: 'a', 2: 'b'}
print(a[1])  # a
print(a[2])  # b

a = {'a': 1, 'b': 2}
print(a['a'])  # 1
print(a['b'])  # 2

## notice
# 딕셔너리의 key 값은 고유한 값이므로,
# 중복되는 key 값을 설정할 경우 하나를 제외한 나머지 것들은 모두 무시된다.
a = {1: 'a', 1: 'b'}
print(a[1])  # b

# 또한 key값으로 리스트 자료형을 사용할 수 없다.
# a = {[1, 2]: 'hi'} # error
# TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
print(a)
# key로 사용할 수 있는 여부는 key가 변하는(mutable)인지, 변하지 않는(immutable) 값인지에 달려 있다.
# 리스트 자료형은 값이 변할 수 있기 때문에 key로 사용할 수 없다.
a = {(1, 2): 'a'}
# 튜플 자료형은 immutable 값이기 때문에 key 사용이 가능하다.
print(a)

## function
# keys
# 딕셔너리 자료형의 key 리스트를 만들 수 있다.
# dict_keys 객체를 반환한다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())  # dict_keys(['name','phone','birth'])

# dict_keys 객체는 다음과 같이 사용할 수 있다.
for k in a.keys():
    print(k)
# name
# phone
# birth

# 리스트로도 변환이 가능하다.
print(list(a.keys()))  # ['name','phone','birth']

# values
# 딕셔너리 자료형의 value 리스트를 만들 수 있다.
# dict_values 객체를 반환한다.
print(a.values())  # dict_values(['pey','010-9999-1234','1118'])

# clear
# 딕셔너리 안의 모든 요소를 삭제한다.
a.clear()
print(a)  # {}

# get
# key로 value 얻기
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))  # pey
print(a['name'])  # pey
print(a.get('phone'))  # 010-9999-1234
print(a['phone'])  # 010-9999-1234
# a.get('name')과 a['name']은 동일한 value를 가져온다.
# 하지만 만약 없는 key를 가져오는 경우
print(a.get('age'))  # None
# print(a['age'])  # error
# KeyError: 'age'
# a['age']의 경우 오류가 발생하게 된다.

# key가 없을 경우 디폴트(default) 값을 대신 가져오게 할 수도 있다.
print(a.get('age', '정보 없음'))  # 정보 없음

# in
# 특정 key가 딕셔너리 안에 있는지 조사하기
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print('name' in a)  # True
print('age' in a)  # False

# pop
# key로 value 얻기
# 해당 항목을 딕셔너리에서 꺼낸 후 삭제한다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
phone = a.pop('phone')
print(phone)  # 010-9999-1234
print(a)  # {'name': 'pey', 'birth': '1118'}
