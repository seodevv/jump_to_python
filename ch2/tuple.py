# tuple.py
# 리스트의 요솟값은 변화가 가능하나
# 튜플의 요솟값은 변화가 불가하다.
# 따라서 값이 바뀌어선 안되는 값에 주로 사용한다.
t1 = ()
t2 = (1,)  # 1개의 요소만 선언할 때도 ,를 붙여줘야 한다.
t3 = (1, 2, 3)
t4 = 1, 2, 3  # 괄호() 생략도 가능하다
t5 = ('a', 'b', ('ab', 'cd'))

t1 = 1, 2, 'a', 'b'
print(t1)
# del t1[0] # error
# TypeError: 'tuple' object doesn't support item deletion
# t1[0] = 'c' # error
# TypeError: 'tuple' object does not support item assignment

t1 = (1, 2, 'a', 'b')
print(t1[0])  # 1
print(t1[3])  # b

# slicing
t1 = (1, 2, 'a', 'b')
print(t1[1:])  # (2,'a','b')

# plus
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # (1,2,'a','b',3,4)

# multiply
t2 = (3, 4)
t3 = t2 * 3
print(t3)  # (3,4,3,4,3,4)

# length
t1 = (1, 2, 'a', 'b')
t1_len = len(t1)
print(t1_len)  # 4

# 튜플은 요솟값을 변경할 수 없기 때문에
# sort, insert, remove, pop 같은 내장 함수가 없다.
