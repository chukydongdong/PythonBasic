list1 = [1,2,3,4,5]
print(list1)
성적list=[95,100]
print(성적list)
list = [1,5,3,6]
print(list[1:3])
print(list[2:])
print(list[:4])
print(list[1])
list = [1,5,3,6]
length = len(list)
print(length)
list = []
print(list)
과목 = ['국어','수학','영어','과학']
print(과목)
무지개 = ['빨강','주황','노랑','초록','파','남','보']
첫번째색 = 무지개[0]
print('무지개의 첫번쨰 색은 {}이다'.format(첫번째색))
무지개 = ['빨강','주황','노랑','초록','파','남','보']
마지막색 = 무지개[6]
print('무지개의 마지막 색은 {}이다'.format(마지막색))
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1+list2
print(list3)
동물 = ['고앙이','강아지']
식물 = ['소나무','단풍나무']
생물 = 동물 + 식물
print(생물*3)
영화 = ['아바타','어벤져스','타이타닉','명랑','겨울왕국']
list=[1,2,3]
list[1] = 10
print(list)
동물 = ['고양이','강아지']
동물.append('사람')
print(동물)
동물 = ['고양이','강아지']
동물.insert(1,'돼지')
print(동물)
동물 = ['고양이','강아지']
del 동물[1]
print(동물)
동물 = ['고양이','강아지']
동물.remove('고양이')
print(동물)
영화.append('겨울왕국2')
print(영화)
영화 = ['아바타','어벤져스','타이타닉','명랑','겨울왕국2']
영화.insert(4,'겨울왕국')
print(영화)
영화 = ['아바타','어벤져스','타이타닉','명랑','겨울왕국2']
del 영화[1]
print(영화)
영화 = ['아바타','어벤져스','타이타닉','명랑','겨울왕국2']
영화.remove('어벤져스')
print(영화)
lang1 = ["C","C++","JAVA"]
lang2 = ["Python","GO","C#"]
langs = lang1 + lang2
print(langs)
tuple = ()
print(tuple)
food = ('떡볶이')
print(food)
rainbow = ('빨','주','노','초','파','남','보')
첫번째색 = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(첫번째색))
무지개 = ['빨강','주황','노랑','초록','파','남','보']
마지막색 = 무지개[6]
print('무지개의 마지막 색은 {}이다'.format(마지막색))
t = (1,2,3,4,5,6,7,8,9,10)
print(t*10)
t = (1,2,3,4,5,6,7,8,9,10)
t2 = t *10
print(t2)
print(len(t2))
영화 = ('아바타','어벤져스','타이타닉','명랑','겨울왕국')
t = ('주먹', '가위', '보')
while True:
    data = int(input("1,2,3을 입력해주세요."))
    if data == -1:
        break
    print(t[data-1])
    # elif data == 1:
    #     print(t[0])
    # elif data == 2:
    #     print(t[1])
    # else:
    #     print(t[2])


















