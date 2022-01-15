name = input('당신의 이름은?')
print(name)

age = int(input('당신의 나이는?'))
print(age)

will = input('당신의 내년 나이는?')
print(will)

print('당신은 ' + name + '이고 ' + str(age) + '살입니다.')
print('당신은' , name, '이고' , age, '살입니다')
print('당신은 {}이고 {}살 입니다.' .format(name, age))

print(' 가위 바위 보 중 하나를 내주세요> ')
# print('가위 바위 보 중 하나를 내주세요> ', end = ' ')
mine = input()
print('mine:' , mine)

mine = input('가위 바위 보 중 하나를 내주세요> ')
print('mine:' , mine)

year = input('지금의 년도는?')
month = input("지금의 달은?")
day = input('지금 일은?')
print("{}/{}/{}" .format(year, month, day))

date = input('오늘 날짜 : ')
year = date[0:4]
month = date[5:7]
day = date[8:10]
print('년 :' , year)
print('월 :' , month)
print('일 :', day)
money = 100
if money == 10000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)
if 3<5:
    print("조건식이 True")
if 3>5:
   print("조건식이 False")

apple = 10
if apple>= 5:
    print("사과를 나누어 먹는다")
else:
    print("걸어 가라")
apple = 3
if apple >= 5:
    print("사과를 나누어 먹는다")
else:
    print("사과를 혼자 먹는다")
money = 10000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
rank = input('몇 등인가요(1 또는 2)?')

if rank == '1': 
    print('TV를 보며 편안하게 쉬세요.')
else:
    print('설거지 당첨!')
number = 15
if number % 3 ==0:
    print("{}는 3의 배수입니다.".format(number))
number = 16
if number % 3 ==0:
    print("{}는 3의 배수입니다.".format(number))
grade = int(input('몇 학년인가요(1~6)?'))
if grade >= 2 and grade <= 4:
    print("햄버거를 주세요")
else:
    print("김밥을 주세요")

money = int(input("가지고 있는돈 :"))
distance = int(input("목적지와의 거리 :"))
weather = input("날씨:")


if money >= 10000 or distance >=100 or weather == '비':
    print("택시를 타고 가라")
else:
    print("걸어가라")
grade = int(input('몇 학년인가요(1~6)?'))
if grade ==2 or grade ==3 or grade ==4 :
    print("햄버거를 주세요")
else:
    print("김밥을 주세요")
