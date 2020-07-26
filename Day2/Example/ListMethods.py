
#Append and insert
country = ["Ind","Aus","US","UK"]
addcoun = ["NZ","Spain"]
country.append(addcoun) # value to append it
print(country)

#print(country[5])
print(country[4])
print(country[4][0])
print(country[4][1])

country.insert(3,addcoun)
print(country)

#Extend - extending two list
country = ["Ind","Aus","US","UK"]
addcoun = ["NZ","Spain","Germany"]
country.extend(addcoun)
print(country)
print(country[5])
print(addcoun)
print(addcoun.clear())
print(addcoun)
addcoun = ["NZ","Spain","Germany","NZ"]
addcountry = addcoun.copy()
print(addcountry)
print(addcoun.count("NZ"))

print(addcoun.pop())
print(addcoun)
addcoun.remove("Spain")
print(addcoun)

addcoun.reverse()
print(addcoun)

country.sort(reverse=True)
print(country)