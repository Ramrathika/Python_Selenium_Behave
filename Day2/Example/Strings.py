s = "Learning Python"

# Multiline String
multiline = """Learning Python is always a fun.
With Python we can able to build applications like
1) UI
2)Desktop """
print(multiline)

# Multiline comments
"""Learning Python is always a fun.
With Python we can able to build applications like
1) UI
2)Desktop """

# Len - find to length of string
s = "LearningPython"
print(len(s))

# indexing
o = 'ORANGE'
print(o[2])

# Slicing
o = 'ORANGE'
print(o[1:4])  # Start and End point
print(o[:4])  # By default it will start point
print(o[2:])  # By default it will treat the end point as last letter

# Negative Indexing
print(o[-2])
print(o[-5])

# Negative Slicing

print(o[-5:-2])

# For each
for f in o:
    print(f)

for i in range(len(o)):
    print(i)
    print(o[i])

# Strip - remove the white spaces

s = "         Learning        Python              "
print(len(s))
print(s.strip())  # it will cut down both left and right
print(len(s.strip()))

# To trim Right spaces
print(s.rstrip())

# To trim left spaces
print(s.lstrip())

print(s.strip())

# lower
s = "learning PYTHON is an art"
print(s.lower())

# upper
print(s.upper())

# Title case
print(s.title())

# captialize
print(s.capitalize())

# casefold
q = "CLAß"
print(q.lower())
print(q.casefold())

# Swapcase
print(s.swapcase())

# Split
h = "Hi.How are you?"
# print(h.split('.')) # list format
spl = h.split('.')
print(spl)
print(type(spl))
print(spl[0])
print(spl[1])

# Reverse a string
t = "Hello"
print(t[::-1])

# Sub string is present or not
h = "Helloooooooo.How are you?"
print('you' in h)  # T/F #membership operator

# Count the number of occurence of char:
print(h.count('o'))

# number of vowels present in a string (a,e,i,o,u)
print(h.count('a') + h.count('e') + h.count('i') + h.count('o') + h.count('u'))

# Concatenation
a = "Hello"
b = "World"
print(a + b)
c = a + b
print(c, "Concatenation")
c = a, b
print(c, "Comma Operator")
print(a, b)

# format
i = 10
strin = 'Sachin Jersey number is'
#print(str+i)
print(strin+format(i))
print(strin+str(i))
print(strin,i)

print("I\'m an Indian.\nAnd am proud to say it as am a \"Indian\"")
