#Question #3
value1 = int(input('Please Enter First Number'))
value2 = int(input('Please Enter 2nd Number'))
if value1 > value2:
    print("Error! Please Enter Valid first Value should less the 2nd value")
else:
    while value1 < value2:
        value1 += 1
        print(value1)