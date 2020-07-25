#Datatypes

#Numbers - int,float, complex
#Strings - string

#Data structures/collections
#list
#set
#dictionary
#Tuple

#Any numbers without decimal point (dot), then its treated as Integer
a = 10
print(a) #10
print(type(a)) #int

#Any numbers with decimal points(dot), then it will treated as Float
pi = 3.14
print(pi)
print(type(pi))

#Complex numbers - real and Imaginary
c = 3+4j
print(c)
print(type(c))

#Strings - double quotes/ single quotes it will be treated as String
'''
s = "10"
p = "India"
str = 'S'
print(type(s))
print(type(p))
print(type(str))
'''
s,p,Str = "10","India","S"
print(type(s),type(p),type(Str))

#isinstance
a = 10
print(isinstance(a,float))

#Type casting
pi = "3.14" #String bcoz I hav given in double quotes
print(type(pi))
f = float(pi)
print(f)
print(type(f))
i = int(f)
print(i)
print(type(i))


#newdatatype(olddatatypevalue) # int(10.05) or int(x) where x = 1.05

x = 99 #int
print(float(x))

y = 10.05
print(int(y))
z = str(y)
print(type(z), z)

s = "10"
print(int(s))

del s
print(s)