#List

li = [1,12,15,4854,54,44]
print(li)

mixedlist = [1,"Orange",2,"Apple",3.14]
print(mixedlist)

fruits = ['Apple','Banana','Orange','Pineapple',"Stawberry"]
print(fruits)
#Indexing
print(fruits[1])
print(fruits[2])
#Negative Indexing
print(fruits[-2])

#Slicing
print(fruits[1:3])

#Loops
for i in fruits:
    print(i)

print(len(fruits))
for f in range(len(fruits)):
    print(fruits[f])

for i in fruits:
    #print(i)
    if 'Pineapple' == i:
        print(len(i))
        break
