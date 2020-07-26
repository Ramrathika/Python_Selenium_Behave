#Set
li = ['US', 'UK', 'Spain', 'NZ', 'Ind', 'Germany', 'Aus', 'Ind', 'Spain']
print(li)
for l in li:
    print(l)
    if l == 'Germany':
        break


se = {'US', 'UK', 'Spain', 'NZ', 'Ind', 'Germany', 'Aus', 'Ind', 'Spain'}
print(se)

for s in se:
    print(s)
    if s == 'Germany':
        #print("India is present")
        break

se.add("Russia")
print(se)
se.add("Ind")
print(se)


Company = {"Microsoft","Google","Apple","Orange"}
Fruits = {"Apple","Orange","Mango","Grapes"}

#union - print all
print(Company.union(Fruits))

#intersection
print(Company.intersection(Fruits))

#Symmetric diff
print(Company.symmetric_difference(Fruits))

#diff
print(Company.difference(Fruits))

#remove - throws error if you dont hav value
#discard - doesnt throw any error

print(Company.remove("Samsung"))