# Question # 6
value1=int(input('enter the number')) 
for i in range(2, int(value1**0.5) + 1):
    if value1 % i == 0:
       print(str(value1)+" Not a Prime number ")
       break
print(str(value1)+" Not a Prime number ")
#  Need To bit discuss
