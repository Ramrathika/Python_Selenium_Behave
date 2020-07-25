#conditional statement

a = 10
b = 5
c = 2

#if (condition) :
#4 spaces/tab
if (a<b) : #a<b is the condition
    print("A s lesser than b")
else:
    print("B is lesser than a")
#Else if

if a<b and a<c:
    print("A is lesser")
elif b<c and b<a:
    print("B is lesser")
else:
    print("C is lesser")

if a<b:
    if a<c:
        print('a is lesser')