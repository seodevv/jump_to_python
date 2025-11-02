### set.py
# 수학의 집합 개념과 동일한 자료형이다.
# 중복을 허용하지 않고 순서가 없는 데이터의 모임이다.
# 교집합, 합집합, 차집합 등의 집합 연산을 쉽게 처리할 수 있다.
s1 = set([1, 2, 3])
print(s1)  # {1,2,3}

s2 = set('Hello')
print(s2)  # {'e','H','l','o'}

s3 = {1, 2, 3}
print(s3)  # {1,2,3}

s4 = {'a', 'b', 'c'}
print(s4)  # {'a', 'b', 'c'}

s5 = set()
print(s5)  # set()

## features
# 중복을 허용하지 않는다.
# - 중복을 허용하지 않는 특징 떄문에 데이터의 중복을 제거하기 위한 필터로도 사용된다.
# 순서가 없다(unordered)
# - 순서가 없기 때문에 인덱싱을 통해 요솟값을 얻을 수 없다.

s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)  # [1,2,3]
print(l1[0])  # 1
t1 = tuple(s1)
print(t1)  # (1,2,3)
print(t1[0])  # 1

## 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)  # {4,5,6}
print(s1.intersection(s2))  # {4,5,6]

# 합집합
print(s1 | s2)  # {1,2,3,4,5,6,7,8,9}
print(s1.union(s2))  # {1,2,3,4,5,6,7,8,9}

# 차집합
print(s1 - s2)  # {1,2,3}
print(s1.difference(s2))  # {1,2,3}

## function
# add
# 1개의 값을 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)  # {1,2,3,4}

# update
# 여러개의 값을 추가
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)  # {1,2,3,4,5,6}

# remove
# 특정 값을 제거
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)  # {1,3}
# s1.remove(4)  # error
# KeyError: 4

# discard
# 특정 값을 제거
# 존재하지 않는 값을 제거하려 할 때 오류가 발생하지 않음
s1 = set([1, 2, 3])
s1.discard(2)
print(s1)  # {1,3}
s1.discard(4)
print(s1)  # {1,3}

# clear
# 모든 값을 제거
s1 = set([1, 2, 3])
s1.clear()
print(s1)  # set()
