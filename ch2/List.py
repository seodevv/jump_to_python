# List.py
odd = [1,3,5,7,9]

a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1,2, ['Life', 'is']]
f = list()

# indexing
a = [1,2,3]
print(a) # [1,2,3]
print(a[0]) # 1
print(a[0] + a[2]) # 4
print(a[-1]) # 3

a = [1,2,3, ['a','b','c']]
print(a[0]) # 1
print(a[-1]) # ['a','b','c']
print(a[3]) # ['a','b','c']

print(a[-1][0]) # a
print(a[-1][1]) # b
print(a[-1][2]) # c

# slicing
a = [1,2,3,4,5]
print(a[0:2]) # [1, 2]

a = '12345'
print(a[0:2]) # 12

a = [1,2,3,4,5]
b = a[:2]
c = a[2:]
print(b) # [1,2]
print(c) # [3,4,5]

a = [1,2,3,['a','b','c'], 4,5]
print(a[2:5]) # [3,['a','b','c'], 4]
print(a[3][:2]) # ['a','b']

# calculation
a = [1,2,3]
b = [4,5,6]
print(a + b) # [1,2,3,4,5,6]

a = [1,2,3]
print(a * 3) # [1,2,3,1,2,3,1,2,3]

# length
a = [1,2,3]
print(len(a)) # 3

# modify
a = [1,2,3]
a[2] = 4
print(a) # [1,2,4]

# delete
a = [1,2,3]
del a[1]
print(a) # [1,3]

a = [1,2,3,4,5]
del a[2:]
print(a) # [1,2]

## function
# append
a = [1,2,3]
a.append(4)
print(a) # [1,2,3,4]

a.append([5,6])
print(a) # [1,2,3,4,[5,6]]

# sort
a = [1,4,3,2]
a.sort()
print(a) # [1,2,3,4]

a = ['a','c','b']
a.sort()
print(a) # ['a','b','c']

# reverse
a = ['a','c','b']
a.reverse()
print(a) # ['b','c','a']

# index
a = [1,2,3]
print(a.index(3)) # 2
print(a.index(1)) # 0
#print(a.index(4)) # error

# insert
a = [1,2,3]
a.insert(0, 4)
print(a) # [4,1,2,3]

a.insert(3,5)
print(a) # [4,1,2,5,3]

# remove
a = [1,2,3,1,2,3]
a.remove(3)
print(a) # [1,2,1,2,3]

a.remove(3)
print(a) # [1,2,1,2]

# pop
a = [1,2,3]
b = a.pop()
print(a) # [1,2]
print(b) # 3

a = [1,2,3]
b = a.pop(1)
print(a) # [1,3]
print(b) # 2

# count
a = [1,2,3,1]
print(a.count(1)) # 2

# extend
a = [1,2,3]
a.extend([4,5]) #  a += [4,5]
print(a) # [1,2,3,4,5]
b = [6, 7]
a.extend(b)
print(a) # [1,2,3,4,5,6,7]

