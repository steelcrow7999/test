import random
import time
##
##print("dice!")
##while 1:
##    value = random.randint(1, 6)
##    print("dice value: %d" %value)
##    time.sleep(2)
##
##i=1
##endvalue = int(input("end Value: "))
##
##while i<=endvalue:
##        print(i)
##        i+=1
##        time.sleep(1)


##i=1
##endvalue = int(input("end Value: "))
##for i in range(endvalue):
##    i+=1
##    print(i)

import sys
sv = int(input("start value: "))
ev = int(input("end value: "))
sum=0
if ev<=sv:
    while sv<=ev:
        print("count: %d" %sv)
        sum+=sv
        sv+=1
        print(sum)
else:   
    sys.exit()
print(sum)
