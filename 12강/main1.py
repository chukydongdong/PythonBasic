class Animal:
    def eat(self):
        print('먹는다')
        
    def die(self):
        print('죽는다')

    def move(self):
        print('움직인다')

class Dog(Animal):
    def bark(self):
        print('멍멍')

    def shake(self):
        print('꼬리를 흔든다')

    def bark2(self):
        print('짓는다')

    
dog = Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()
dog.die()
dog.bark2()
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')
        
    def move(self):
        print('움직인다')

class Dog(Animal):

    def __init__(self,name,age,owner):
        super().__init__(name,age)
        self.owner = owner
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence = '이름:{}, 나이:{}, 주인:{}'.format(self.name, self.age,self.owner)
        return sentence

animal = Animal('동물',1)
animal.eat()
dog = Dog('코코',2,'홍길동')
dog2 = Dog('코코',2,'홍길동')
print(dog.name,dog.age,dog.owner)
print(dog)
print(dog2.name,dog2.age, dog2.owner)
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')
        
    def move(self):
        print('움직인다')
        
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age)
        return sentence
class Bird(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def fly(self):
        print('날아오르라 주작이여')
    def eatearthworm(self):
        print('지렁이 맛있다')
    def __str__(self):
        sentence = '이름:{}, 나이:{}'.format(self.name, self.age )
        return sentence

bird=Bird('새',3)
print(dog)
print(bird)

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def home(self):
        print('집')
    def play(self):
        print('놀자')
    def __str__(self):
        s = '이름:{},나이:{}'.format(self.name, self.age)
        return s
class Teacher(Human):
    def __init__(self,name,age):
        super().__init__(name,age)
    def study(self):
        print('공부를 잘한다')
    def school(self):
        print('학교에 있는다')
class Student(Human):
    def __init__(self,name,age):
        super().__init__(name,age)
    def study(self):
        print('공부를 한다')
    def homework(self):
        print('숙제를 한다')
teacher = Teacher('김숙이',32)
student = Student('김동현',13)
print(teacher)
print(student)



    









