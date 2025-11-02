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


name = '홍길동'
result = number_handler(name)
print(f'{name}님의 성별 코드는 {"남자" if result[1][0] == "1" else "여자"}입니다.')
