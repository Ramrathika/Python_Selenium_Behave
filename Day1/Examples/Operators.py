#Arithmetic Operators

a = 4
b = 4

print(a+b) # Addition
print(a-b) #Sub
print(a*b) #Mul
print(a/b) #division - float
print(a//b) # quotient - int output
print(a%b) # remainder
print(a**b) #power off - exponential form

#Comparison operators/conditional operators

p = 5
q = 3
print(p == q) #==-> whether p is equal to q
print(p!=q)
print(p<q)
print(p>q)
print(p<=q)
print(p>=q)

a = "India"
b = "india"
print(a == b)


#Assignment operators - not very important

a = 10 # = is assignment operators
a += 10 #a = a+10
print(a)
a -= 10
print(a)

#logical operators - and / or / not -it very imp
i = 10
j = 15
k = 8

print(i<j and i<k)
print(i<j or i<k)

# T and T = T
# T and F = F
# F and T = F
# F and F = F

# T or T = T
# T or F = T
# F or T = T
# F or F = F

# Bitwise operation - for binary operations - not important

#Membership - in - contains loops, list everywher

string = "I am an Indian"
substr = "Pak"

print(substr in string)
print("India" in "I am an Indian")

print(substr not in string)

#identity -> is -> == and is not -> !=

a = "India"
b = "India"
print(a is b)
print(a == b)

print(a is not b)