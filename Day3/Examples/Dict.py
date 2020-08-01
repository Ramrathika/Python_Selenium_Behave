#Dict is to store in Key and value pair
#Dict is indexed, changable and unordered
#Dict can store heterogeneous value


newdict = {
    "Virat":18,
    7: "Dhoni"
}

print(newdict.get("Virat"))

#Accessing a dict
thisdict = {

    "Fruit": "Mango",
    "Vegetable":"Carrot",
    "Number":"9",
    "Color":"Blue",
    2020: "Year"
}

#Accessing in normal way
print(thisdict)

#Accessing particular value
#Indexing wnt work #KeyError:
#print(thisdict[2])

print(thisdict["Number"])
#Using get
print(thisdict.get("Number"))

#For loop
#Accessing a dict
thisdict = {
    "Fruit": "Mango",
    "Vegetable":"Carrot",
    "Number":"9",
    "Number":"10",
    "Number": "11",
    "Color":"Blue",
    2020: "Year"
}
#Keys
for i in thisdict:
    print(i)
print("---------------------")

#values
for t in thisdict:
    print(thisdict[t]) #print(thisdict.get(t))
print("---------------------")

#keys
for i in thisdict.keys():
    print(i)
print("---------------------")
#Values
for v in thisdict.values():
    print(v)
print("---------------------")

#items
for i in thisdict.items():
    #print(i)
    if "Carrot" in i:
        print("Carrot is present")

print("---------------------")

print(thisdict)
print("---------------------")
thisdict["Number"] = "19"
print("---------------------")
print(thisdict)
print("---------------------")

thisdict = {
    "Fruit": "Mango",
    "Vegetable":"Carrot",
    "Number":"9",
    "Number":"10",
    "Number": "11",
    "Color":"Blue",
    2020: "Year"
}
print(thisdict)
print("---------------------")

newdict = thisdict.copy()
print(newdict)

newdict.clear()
print(newdict)
print("---------------------")

student = {
    "Ram": 75,
    "Sita":99,
    "Laxman":50

}

newstudent = student.fromkeys(student,10000)
print(newstudent)
print("---------------------")

#Pop # remove the mentioned key
newstudent.pop("Sita")
print(newstudent)

#Popitem # remove the last value
newstudent.popitem()
print(newstudent)

#Update
newstudent.update({"Ravan":"15"})
print(newstudent)
newstudent.update({"Ravanan":"1955"})
print(newstudent)

#Setdefault
c= newstudent.setdefault("Ravan","173")
print(newstudent)