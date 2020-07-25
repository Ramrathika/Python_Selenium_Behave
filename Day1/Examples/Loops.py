#For loop = it needs a stop point
#While loop - stop point is not mandatory, until the conditions satisfices the code will be executed

#numbers = 1-10

for i in range (1,11,1): #Start, stop and step (incrementation)
    print(i)
print('-------------------')

#start will be 0 Optional
#Step will be 1 -optional
for i in range(15): #stop- start and step
    print(i)
print('-------------------')
for i in range(50,100):
    print(i)

for i in range(50,500,50): #50- start value, 500- end value, 50+50,100+50, 150+50
    print(i)

for i in range(100,5,-25):
    print(i)

#for each loop - string, list etc
sInd = "India"
for s in sInd:
    print(s)

for s in range(len(sInd)):
    print(sInd[s])


li = [10,20,30,45,80,760]
for l in li:
    print(l)


sInd = "India"
for s in sInd:
   # print(s)
    if s == 'd':
        print(s)
        break

for i in range (150):
    if i < 10:
        print(i)
        break