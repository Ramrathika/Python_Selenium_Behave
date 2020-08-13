class Dog:

    #data
    name = "Tommy"
    color = "Brown"

    #functions
    def toBark(self):
        #print("Bark at Strangers")
        return "Bark at strangers"
    def Eat(self):
        print("Eat at right time")


d = Dog()#d is object
print(d.name)
print(d.color)
d.toBark()
print(d.toBark())

class rectangle:
    #length = 10
    def __init__(self,length,breadth, cost):
        self.length = length
        self.breadth = breadth
        self.cost = cost

    def area(self):
        return self.length*self.breadth

    def calcost(self):
        area = self.area()
        print(area)
        return area * self.cost

r = rectangle(15,20,10)
r1 = rectangle(17,30,15)
print(r.area())
print(r.calcost())

print(r1.area())
print(r1.calcost())

class student:

    def __init__(self,name,rollnum,age):
        self.name = name
        self.rollnum = rollnum
        self.age = age

    def marks(self,english,language,maths):
        self.english = english
        self.language = language
        self.maths = maths
        return english + language + maths

    def calculategrade(self):

        marks = self.marks(self.english,self.language,self.maths)
        print(marks)
        if (marks//3) >= 80:
            return "First class with distinction"

        elif (marks // 3) >=60:
            return "First class"

        elif (marks // 3) <= 35:
            return "Fail"
        else:
            return "Second class"

print('********************')
student1 = student("Virat","1955","10")
print(student1.marks(75,50,80))
print(student1.calculategrade())
print('********************')

student2 = student("Rohit","2178","10")
print(student2.marks(35,67,70))
print(student2.calculategrade())
print('********************')


student3 = student("Dhoni","7070","10")
print(student3.marks(35,15,20))
print(student3.calculategrade())
print('********************')

class animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animals will sleep at night")

class dog(animal):
    def bark(self):
        print("Dog is barking")

    def sleep(self):
        print("Dog will sleep at day")

class bulldog(dog):
    def bark(self):
        print("It will bark loudly")
    def bite(self):
        print("It wil bite strangers")

class cat(animal):
    def chasing(self):
        print("Cat is chasing rats")

print("************dog**************")

d = dog()
d.eat()
d.bark()
d.sleep()
print("************cat**************")
c = cat()
c.eat()
c.chasing()
c.sleep()
print("************bulldog**************")
b = bulldog()
b.eat() #animal
b.sleep() #dog
b.bite() #bulldog
b.bark() #overrided so captured from bull dog


#Multiple
class summation:
    def sum(self,a,b):
        return a+b

class multiplication:
    def mul(self,a,b):
        return a*b

class derived(summation,multiplication):
    def div(self,a,b):

        return a//b

d = derived()
print(d.sum(5,10))
print(d.mul(5,10))
print(d.div(10,5))

# access modifiers

#public
class employee:
    def __init__(self,name,empnum):
        self.name = name
        self.empnum = empnum

e = employee("Mahi","10")
print('***************Public Access Modifiers*******************')
print(e.empnum)
print(e.name)


#protected
class employee:
    def __init__(self,name,empnum):
        self._name = name
        self._empnum = empnum

    def employee_fun(self,hobbies):
        self._hobbies = hobbies
        return "Hobbies-->"+hobbies
e = employee("Mahi","10")
print('***************Protected Access Modifiers*******************')
print(e._empnum)
print(e._name)


class bank(employee):
    def fun(self):
        print("blank")

b = bank("Sachin",1)
print(b._empnum)
print(b._name)
print(b.employee_fun("playying cricket"))
'''
#private
class employee:
    def __init__(self,name,empnum):
        self.__name = name
        self.__empnum = empnum

e = employee("Mahi","10")
print('***************Private Access Modifiers*******************')
print(e.__empnum)
print(e.__name)

'''

class addition:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        #print(a+b)
    def add(self):
        return self.a+self.b

a = addition(2,3)
b = addition("Hi","Hello")
c = addition(15.50,30.7999)
