dic = {}
print(dic)
dic = {'이름' : '홍길동', '나이':12, '성별':'남성','생일':'12월 1일'}
print(dic)

ice = {"메로나":1000,"비비빅":1200,'빵빠레':1800}
print(ice)

ice = {"메로나":1000,"비비빅":1200,'빵빠레':1800}
ice["죠스바"]=1200
ice["월드콘"]=1500
print(ice)

ice = {"메로나":1000,"비비빅":1200,'빵빠레':1800,"죠스바":1200,"월드콘":1500}
print("메로나 가격:",ice["메로나"])
ice = {"메로나":1000,"비비빅":1200,'빵빠레':1800,"죠스바":1200,"월드콘":1500}
ice["메로나"]=1300
print(ice)

ice = {"메로나":1000,"비비빅":1200,'빵빠레':1800,"죠스바":1200,"월드콘":1500}
del ice["빵빠레"]
print(ice)
 
ice = {"메로나":[1000,2],"비비빅":[1200,24],'빵빠레':[1800,39],"죠스바":[1200,26],"월드콘":[1500,33]}
print(ice)
ice = {"메로나":[1000,2],"비비빅":[1200,24],'빵빠레':[1800,39],"죠스바":[1200,26],"월드콘":[1500,33]}
print(ice["메로나"][0],"원")
print(ice["메로나"][1],"개")
ice = {"메로나":[1000,20],
       "비비빅":[1200,3],
       "스크류바":[1800,100]}
ice["월드콘"] = [500,7]
print(ice)

days = { '1월':31,'2월':28,'3월':31}
print(days)
days = {'1월':31, '2월':28, '3월':31}
days['2월'] = 29
print(days)
days = { '1월':31,'2월':28,'3월':31}
print(days)
days = {'1월':31, '2월':28, '3월':31}
days['2월'] = 29
days['13월'] = 31
del days['13월']
print(days)


,


