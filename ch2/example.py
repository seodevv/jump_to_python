### example.py
## Q1 평균 점수 구하기
# 홍길동 씨의 과목별 점수는 다음과 같다. 평균 점수를 구하자
students = [
    {
        "name": "홍길동",
        "grade": {
            "국어": 80, "영어": 75, "수학": 55
        }
    },
    {
        "name": "홍갈동",
        "grade": {
            "국어": 75, "영어": 65, "수학": 45
        }
    }
]

# sum = 0
# count = 0
# for student in students:
#     if student.get('name') == '홍길동':
#         for score in student.get('grade').values():
#             sum += score
#             count += 1
#
# print(sum / count)

for s in students:
    if s.get('name') == "홍길동":
        scores = s['grade'].values()  # dict_values([80, 75, 55])
        avg = sum(scores) / len(scores)
        print(f"{s['name']}의 평균 점수는 {avg:.2f}점입니다.")
        break


## Q2 홀수, 짝수 판별하기
# 자연수 13 이 홀수인지, 짝수인지 판별할 수 있는 방법에 대해 말해보기
# 2로 나눈 나머지 값을 체킹
def is_even(num):
    if (num % 2 == 0):
        return '짝수입니다.'
    else:
        return '홀수입니다.'


print(is_even(13))  # 홀수입니다.

## Q3 주민등록 나누기
# 홍길동  씨의 주민등록번호는 881120-1068234 이다.
# 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
students = [
    {
        'name': "홍길동",
        'number': "881120-1068234"
    },
    {
        'name': "홍갈동",
        'number': "881120-1068234"
    }
]

from typing import List


def number_handler(name: str) -> List[str]:
    for s in students:
        if name == s.get('name'):
            [a, b] = s.get('number').split('-')
            print(f'{name}님의 생년월일은 {a}입니다.')
            print(f'{name}님의 주민번호 뒷자리는 {b}입니다.')
            return [a, b]


## Q4 주민등록번호 인덱싱
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다.
# 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.
name = '홍길동'
result = number_handler(name)
print(f'{name}님의 성별 코드는 {result[1][0]}:{"남자" if result[1][0] == "1" else "여자"}입니다.')

## Q5 문자열 바꾸기
# 다음과 같은 문자열 a:b:c:d가 있다.
# 문자열의 replace 함수를 사용하여 a#b#c#d로 변경해 출력해보자.
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)  # "a#b#c#d"

## Q6 리스트 역순 정렬하기
# [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자.
a = [1, 3, 5, 4, 2]
a.sort(reverse=True)
print(a)

## Q7 리스트를 문자열로 만들기
# ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어보자.
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

## Q8 튜플 더하기
# (1,2,3) 튜플에 값 4 를 추가하여 (1,2,3,4)를 만든 후 출력해보자.
a = (1, 2, 3)
a = a + (4,)
print(a)

## Q9 딕셔너리의 키
# 다음과 같은 딕셔너리가 a가 있다.
a = dict()  # {}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해보자.
a['name'] = 'python'  # 에러 발생하지 않음
a[('a',)] = 'python'  # 에러 발생하지 않음. key로 immutable은 가능함
# a[[1]] = 'python'  # 에러 발생함. key가 mutable이 되면 안됌
a[259] = 'python'  # 에러 발생하지 않음

## Q10 딕셔너리 값 추출하기
# 딕셔너리 a에서 'B'에 해당하는 값을 추출해보자.
# pop 함수를 사용해보자.
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)  # {'A': 90, 'C': 70}
print(result)  # 80

## Q11 리스트에서 중복 제거하기
# a 리스트에서 중복 숫자를 제거해보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = list(set(a))
print(b)  # [1,2,3,4,5]

## Q12 파이썬 변수
# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
# 다음과 같이 a,b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까?
# 그리고 이러 결과가 나타나는 이유를 설명해보자.
a = b = [1, 2, 3]
a[1] = 4
print(b)  # [1,4,3]
print(id(a), id(b))  # 동일한 메모리 참조
print(a is b)  # True
# 동일한 메모리를 참조하기 때문.
# 다른 메모리를 참조하려면 copy 모듈이나 a[:]를 사용해야한다.
