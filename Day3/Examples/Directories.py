import os
import sys

print(os.getcwd())

os.chdir("C:\\Users\\Vignesh\\OneDrive\\Desktop\\Selenium Tutorial\\Python tutorial\\Python\\File Handling")
print(os.getcwd())

print(os.listdir())

for l in os.listdir():
    if "Directory.txt" == l:
        print("Directory.txt s available")
        f = open(l,"a")#r- read,a-append,w-write, x-create
        f.write("Automation Bytes")
        f.close()