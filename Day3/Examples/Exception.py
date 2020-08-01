import traceback
import time

dec  = "Example"
try:
    print(dec)
except:
    print("Print is failed")
    traceback.print_exc()

finally:
    print("Finally")

#print("hello world")

print('-----------------------------------------------------')

#dec  = "Example"
try:
    print(december)
except:
    print("Print is failed")
    traceback.print_exc()

finally:
    print("Finally")
#print("hello world")


try:
    print("Hello")
finally:
    print("Finnally")

print("-----------------------")
try:

    print(100/0)

except:
    print("Anything by zero is not divisble")
    traceback.print_exc()


x = -10
if x < 0:
    raise Exception("Provide number greater than zero")