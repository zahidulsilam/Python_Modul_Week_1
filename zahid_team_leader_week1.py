#Question #1
# i=0
# for i in range(1,13):
#     print(i)

#Quesion #2
# user_input = input('Please Enter Number')
#i = 1
# for i in range(i,int(user_input)):
#     if i%2 == 0:
#         print(i)
# while i <= int(user_input):
#     i += 1
#     if i%2 == 0:
#         print(i)

#Question #3
# value1 = int(input('Please Enter First Number'))
# value2 = int(input('Please Enter 2nd Number'))
# if value1 > value2:
#     print("Error! Please Enter Valid first Value should less the 2nd value")
# else:
#     while value1 < value2:
#         value1 += 1
#         print(value1)

# Question #4
# value1 = int(input('Please Enter Number'))
# if value1 % 2 == 0:
#     print('Even Number')
# else:
#     print("Odd Number")

#Question #5

# number = int(input('Please Enter Number'))
# factorial = 1
# for i in range(2, number + 1):
#     factorial *= i
# print(factorial)


# Question # 6
# value1=int(input('enter the number')) 
# for i in range(2, int(value1**0.5) + 1):
#     if value1 % i == 0:
#        print(str(value1)+" Not a Prime number ")
#        break
# print(str(value1)+" Not a Prime number ") Need To bit discuss


#Question # 7
# number = int(input('Please Enter Number'))
# i=0
# numer_calc = 0
# add_number = 1
# while i < number:
#    final_number = numer_calc + add_number
#    print(numer_calc) 
#    numer_calc = add_number
#    add_number = final_number
#    i += 1
   


#Question no 8

# text = input('Please Enter Word')
# tlen = len(text) - 1
# new_text = ''
# for i in range(tlen, -1, -1):
#     new_text = new_text+text[i]
# print(new_text)  


# #Question # 9

# text = input('Please Enter Word')
# revers_word = text[::-1]
# if text == revers_word:
#     print("word is a palindrome")
# else:
#     print("word is Not a palindrome")


# #Question # 10
# weight = int(input('Please Enter Weight'))
# height = int(input('Please Enter Height in cm'))
# # convert cm to meters
# meter = height/100
# BMI = round(weight/(meter**2))
# if(BMI < 25):
#     print("You are Week!")
# elif(BMI >= 25 and BMI <= 30):
#     print("You are Normal!")
# elif(BMI > 30  and BMI <= 40):
#     print("You are over weight!")
# else:
#     print("You are obese weight!")


#Question # 11
# number1 = int(input('Please Enter first number'))
# number2 = int(input('Please Enter 2nd number'))
# number3 = int(input('Please Enter 3rd number'))
# if number1 > number2 and number1 > number3:
#     print("number1 is Largest ")
# elif number2 > number1 and number2 > number3:
#     print("number2 is Largest ")
# else:
#     print("Number2 is Largest")

#Question no 12

for i in range(1,5):
    seconde_term = float(input(f"Enter midterm grade Subject {i}:"))
    final_term = float(input(f"Enter final term grade {i}:"))
    average_marks_subject = (seconde_term * 0.4) + (final_term * 0.6)
    if average_marks_subject >= 50:
        final_result = "SUCCESSFUL"
    else:
        final_result = "FAILED"
    print(f"Averege Marks{average_marks_subject:.2f} Result {final_result}")