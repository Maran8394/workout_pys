
import math,random

otp = ""
for i in range(6):
    otp+=str(math.floor(random.randrange(0,9)))
print(otp)
print(type(int(otp)))

