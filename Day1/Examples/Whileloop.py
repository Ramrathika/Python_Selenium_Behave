#1-10

i = 1#start point
while i<=10: #condition
    print(i)
    i = i + 2 #step


#Reversing a nUmber

number = 159 # number%10 - * 10 + reverse
#output = 19754
reverse = 0
while(number>0):
    remainder = number%10 # output - 9, 5 , 1
    reverse = (reverse*10)+remainder # (0*10)+9 = 9 - 90+5 = 95 = 95*10 = 950+1
    number = number // 10 # 159//10 = 15  , 1 , 0

print(reverse)