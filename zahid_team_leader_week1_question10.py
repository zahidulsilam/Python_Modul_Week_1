#Question no 10

weight = int(input('Please Enter Weight'))
height = int(input('Please Enter Height in cm'))
# convert cm to meters
meter = height/100
BMI = round(weight/(meter**2))
if(BMI < 25):
    print("You are Week!")
elif(BMI >= 25 and BMI <= 30):
    print("You are Normal!")
elif(BMI > 30  and BMI <= 40):
    print("You are over weight!")
else:
    print("You are obese weight!")
