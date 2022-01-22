pizza = input('피자 가게가 열렸나요(예/아니요)?')
chicken = input('치킨 가게가 열렸나요(예/아니요)?')
편의점 = input('편의점이 열렸나요(예/아니요)?')
if pizza == '예':
    print('피자가게로 가자')
elif chicken == '예':
    print('치킨 가게로 가자')
elif 편의점== '예':
    print('편의점에서 라면을 먹자')
else:
    print('집으로 가자')
data = int(input("입력값: "))
if data + 20 < 255:
    print(data + 20)
else:
    print('255')
data = int(input("입력값: "))
if 0 < data - 20 < 255:
    print(data - 20)
elif data - 20 < 0:
    print('0')
else:
    print('255')
score = int(input("입력값:"))
if  80 < score < 101:
    print('A등급')
elif 60 < score < 81 :
    print('B등급')
elif 40 < score < 61 :
    print('C등급')
elif 20 < score < 41 :
    print('D등급')
else :
    print('E등급')
num1 = int(input("number1: "))
num2 = int(input("number2: "))
num3 = int(input("number3: "))
if num1 < num3 and num2 < num3 :
    print(num3)
elif num1 > num3 and num1 > num2 :
    print(num1)
else :
    print(num2)
주민번호 = input("주민등록번호: ")
if 주민번호[7] == '1' or 주민번호[7] == '3' :
    print('남자')
else:
    print('여자')

def getGrade(score) :
    if  80 < score < 101:
        print('grade is A')
    elif 60 < score < 81 :
        print('grade is B')
    elif 40 < score < 61 :
        print('grade is C')
    elif 20 < score < 41 :
        print('grade is D')
    else :
        print('grade is E')


score = int(input("입력값:"))
getGrade(score)
getGrade(88)
getGrade(2)
getGrade(70)
hit = 0
while hit < 10:
    hit =hit +1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print('나무가 넘어갔습니다')
    elif hit == 8:
        print('나무가 곧 넘어갈것 같습니다.')
    elif hit == 6:
        print('나뭇잎 떨어짐')
    elif hit == 4:
        print('나뭇잎 떨어짐')
    elif hit == 2:
        print('나뭇잎 떨어짐')
