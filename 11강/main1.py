class Dog:
    name = '코코'
    age = 2
    die = 13
    def bark(self):
        print('멍멍')    
    def move(self):
        print('움직인다')
    def eat(self):
        print('냠냠')
    
dog1 = Dog()
dog1.bark()
dog1.move()
dog1.eat()
dog2 = Dog()
dog2.bark()
dog2.move()
dog2.eat()
class Dog:
   name = '코코'
age = 2
die = 13
def bark(self):
    print('멍멍')    
def move(self):
    print('움직인다')
def eat(self):
    print('냠냠')
dog1 = Dog()
dog1.name = '코코'
dog1.age = 2
dog2 = Dog()
dog2.name = '두리'
dog2.age = 5
dog3 = Dog()
dog3.name = '하리'
dog3.age = 6
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
print(dog3.name, dog3.age)
class Dog:
    def __init__(self,name,age):
       self.name = name
       self.age = age
   
    def bark(self):
        print('멍멍')    
    def move(self):
        print('움직인다')
    def eat(self):
        print('냠냠')
    
dog1=Dog('코코',2)
dog2=Dog('두리',5)
dog3=Dog('하리',6)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
print(dog3.name, dog3.age)
class Dog:
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def bark(self):
        print('{}가 멍멍'.format(self.name))
    def move(self):
        print('{}가 움직인다'.format(self.name))
dog1 = Dog('코코',2)
dog2=Dog('두리',5)
dog3=Dog('하리',6)
dog1.bark()
dog2.bark()
dog3.bark()
dog1.move()
dog2.move()
dog3.move()
result=0

def 더하기(num):
    global result
    result += num
    return result
print(더하기(3))
print(더하기(4))
class Caculator:
    def __init__(self):
        self.result = 0

    def 더하기(self, num):
        self.result += num
        return self.result

call = Caculator()

print(call.더하기(3))
print(call.더하기(4))
class Dog:
    def __init__(self,name,age):
       self.name = name
       self.age = age
   
    def bark(self):
        print('멍멍')    
    def move(self):
        print('움직인다')
    def __str__(self):
        sentence = '이름:{},나이:{}'.format(self.name,self.age)
        return sentence

dog1 = Dog('코코',2)
dog2=Dog('두리',5)
dog3=Dog('하리',6)
print(dog1)
print(dog2)
print(dog3)
class Caculator:
    def __init__(self):
        self.result = 0

    def 더하기(self, num) :
        self.result +=num
        return self.result

    def 빼기(self,num):
        self.result -=num
        return self.result
call =  Caculator()
print(call.더하기(3))
print(call.더하기(4))
print(call.빼기(1))
class Caculator:
    def __init__(self):
        self.result = 0
    def 더하기(self, num):
        self.result += num
        return self.result
    def 빼기(self, num):
        self.result-=num
        return self.result

cal1 = Caculator()
cal2 = Caculator()
print(cal1.더하기(3))
print(cal2.더하기(3))
print(cal1.더하기(4))
print(cal2.더하기(4))
print(cal1.빼기(1))
print(cal2.빼기(1))

class Caculator:
    def __init__(self):
        self.result = 0
    def 더하기(self, num):
        self.result += num
        return self.result
    def 빼기(self, num):
        self.result-=num
        return self.result
    def 곱하기(self, num):
        self.result*=num
        return self.result
    def 나누기(self, num):
        self.result/=num
        return self.result

cal1 = Caculator()
cal2 = Caculator()

print(cal2.더하기(4))
print(cal2.더하기(3))
print(cal1.더하기(3))
print(cal1.더하기(4))
print(cal1.빼기(1))
print(cal2.빼기(1))
print(cal2.곱하기(4))
print(cal2.곱하기(4))
print(cal1.나누기(2))
print(cal1.나누기(2))
