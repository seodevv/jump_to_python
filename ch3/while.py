### while.py
# 문장을 반복해서 수행해야 할 경우 while 문을 사용한다.
# 그래서 while 문을 '반복문'이라고도 부른다.

## structure
'''
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
    ...
'''
# while 문은 조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행된다.
'''열번 찍어 안 넘어가는 나무 없다.'''
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print(f"나무를 {treeHit}번 찍었습니다.")

# 나무를 1번 찍었습니다.
# 나무를 2번 찍었습니다.
# ...
# 나무를 9번 찍었습니다.
# 나무를 10번 찍었습니다.

## make while
# 조건문을 통해 while을 종료하는 경우
# 프롬프트에서 선택하여 4를 선택하면 프로그램을 종료한다.
prompt = """
   1. Add
   2. Del
   3. List
   4. Quit
   
   Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

# break를 통해 while를 종료하는 경우
# 커피가 다 떨어지면 break를 통해 while문을 종료한다.
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print('남은 커피의 양은 %d입니다.' % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 실제 자판기의 작동 과정과 비슷하게 만든 예
coffee = 10
while True:
    money = int(input('돈을 넣어 주세요:'))
    if money == 0:
        print("돈을 넣지 않아. 판매를 중지합니다.")
        break;
    elif money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break;

## Go back to the beginning of the while loop
# while 문의 중간에서 다시 맨 처음으로 돌아가게 싶은 경우가 있다.
# 그런 경우 comtinue 문을 사용하면 된다.
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

## infinite loop
# 말 그대로 무한히 반복한다는 의미이다.
# 무한 루프의 기본 형태는 다음과 같다.
'''
while True:
    수행할_문장1
    수행할_문장2
    ...
'''

# while True:
#     print("Crtl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

## while-else 문
# 파이썬의 wilhe 문에는 else 절을 사용할 수 있다.
# while-else 문은 while 문이 정상적으로 종료되었을 때(break로 빠져나가지 않았을 때) else 절이 실행된다.
count = 0
while count < 3:
    print(f"카운트: {count}")
    count += 1
else:
    print('while 문이 정상 종료되었습니다.')

# 하지만 break 문으로 while 문을 종료하면 else 절은 실행되지 않는다.
count = 0
while count < 5:
    if count == 2:
        break;
    print(f'카운트 : {count}')
    count += 1
else:
    print("while 문이 정상 종료되었습니디")

## nested while statement
# while 문 안에 또 다른 while 문을 사용할 수 있다.
# 이를 중첩된 while 문이라고 한다.
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f'i={i}, j={j}')
        j += 1
    i += 1
