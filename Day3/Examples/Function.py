import math

def Sample():
    print("Sample Function")
Sample()

def example4doc():
    """This is an example function
    Here we will be seeing how to use
    python docs"""
    print("An example to print python docs")
print(example4doc.__doc__)
example4doc()

print("_________________________")

#add

def add(a,b,c):
    d = a+b+c
    return d

print(add(1,5,9))
print(add("Hi","I'am","Vignesh"))

print(math.factorial(5))

#Recurisive
def rec(num):
    if num == 1:
        return 1
    else:
       # print(num*(rec(num-1)))
        return (num*(rec(num-1)))

#print(rec(5))
rec(5)

#lambda
#x = variable
#a,b = arguments
#a+b
x = lambda a,b,c,d : (a+b)*(c+d)
print(x(5,6,2,4))

sample = lambda sample: print("sample")
print(sample(sample))

def myfun(num):
    return lambda a: a*num

functionname = myfun(2) #function name
print(functionname(5)) #lampda value is 5

def myfun(num1,num2):
    print(num1*num2)
myfun(2,5)