#Question no 11

number1 = int(input('Please Enter first number'))
number2 = int(input('Please Enter 2nd number'))
number3 = int(input('Please Enter 3rd number'))
if number1 > number2 and number1 > number3:
    print("number1 is Largest ")
elif number2 > number1 and number2 > number3:
    print("number2 is Largest ")
else:
    print("Number2 is Largest")
