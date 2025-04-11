# Q1: Write a Python code that prints numbers from 1 to 10 on the screen.

for i in range(1, 11):
    print(i)

# Q2:Take a number input from the user and write a Python program that prints even numbers up to this number on the screen.
# Do this first with 'for' and then with 'while' loops.
user_input = input('Please Enter Number')
i=0
for i in range(i,int(user_input)):
    if i%2 == 0:
        print(i)

i = 0
user_input = input('Please Enter Number')
while i <= int(user_input):
    if i == 0 :
        print(i)
    i += 1
    if i%2 == 0 :
        if i > int (user_input):
            break
        print(i)

# Q3: Write a Python code that receives a start and end value from the user
# and prints all the numbers between these values ​​(including the end value) on the screen.
Start_Value = input('Enter a start Number ')
End_Value = input('Enter an End Number')
if int(Start_Value) > int(End_Value):
    print("End Number Should be Biger Than Start Number ")
    Start_Value = input('Enter a start Number ')
    End_Value = input('Enter an End Number')
    x = range(int(Start_Value), int(End_Value) + 1)
    for n in x:
        print(n)
else:
    x = range(int(Start_Value), int(End_Value) + 1)
    for n in x:
        print(n)

# Q4: Get a number from the user and write a Python code that prints whether this number is odd or even
user_input = int(input('Inter integer number'))
if user_input % 2 == 0 :
    print("This Number is Even")
else:
    print('This Number is Odd')

# Q5: Write a Python program that takes a positive integer input from the user and calculates its factorial.
# Factorial is the product of all positive integers between a number itself and 1.
# For example: if the user entered 5, the program should give the following output:
# Enter a number from the user: 5
# Factorial: 120
number = int(input("Enter a positive integer to calculate its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print("The factorial of", number , " is:", factorial)

# Q6: Write a Python code that receives a number from the user and checks whether this number is prime.
num = int (input("Insert Positive integer Number"))
if num < 0:
    print("The Number in negative , inter a positive Number " )
elif num == 0 or num == 1 :
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")

            break
    else:
        print(num, "is a prime number")

# Q7: How to create a loop that calculates the Fibonacci sequence
# and returns the result as a list containing numbers up to a certain limit?
Num_terms = int(input("How many terms? "))

# first two terms
x = 0
y = 1

num_list =[x]
# check if the number of terms is valid
if Num_terms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif Num_terms == 1:
   print("Fibonacci sequence upto",Num_terms,":",num_list)

# generate fibonacci sequence
else:
    num_list = [x,y]
    count=2
    while count < Num_terms:
       z = x + y
       num_list.append(z)
       # update values
       x = y
       y = z
       count +=1
    print("Fibonacci sequence upto",Num_terms,":",num_list)

# Q8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.
word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
    # Print each character from the word in reverse order without a new line (end="")
    print(word[char], end="")

# Q9: How to create a combination of loop and conditional statement that takes a word input from the user 
# and checks whether that word is a palindrome (the same when read backwards)?
word = input("Inter a word to check if it is palindrome ")
first = 0
length = len(word)
last = length
half = int(length/ 2)

while half > 0 :
    if word[first] != word[last-1]:
        print("This word is not  palindrome")
        
        break
    first += 1
    last -= 1
    half -= 1
if half <= 1:
    print("This word is a palindrome")

 #Question 10: Write the code that calculates the person's weight index and returns the result as underweight,
 #  overweight or overweight according to the index value. (You can look on the internet for the weight index calculation)
#To do this, ask the user for their weight and height measurements. weight index
# If it is below 25, it is weak,
# Between 25-30 is normal,
# If you are over 30-40, you are overweight.
# If you are over 40, you are overweight.

kg = float(input("Please enter your weight in Kg and more than zero "))
while kg <= 0 :
    kg = float(input("Please re-enter your weight in Kg and more than zero"))

le = float(input('Please enter your height in M and more than zero'))
while le <= 0 :
    le = float(input('Please re-enter your height in M and more than zero '))

bmi = le / (kg *kg)
if bmi > 40 :(print("You are Highly overweight."))
elif bmi > 30 :
    print('You are Overweight.')
elif bmi >= 25 :
    print('Your Weight is Normal ')
else: print(' You are underweight ')

# Q 11: How to write a Python program that finds the largest of three numbers
#  entered by a user?
x = float(input("put the first num" ))
y = float(input("put the second num" ))
z= float(input("put the third num" ))
largest = x
if y >= x :
    largest = y
    if y <= z :
        largest = z
elif x<= z:
    largest = z
print("The largest Num is :", largest)

#  Q12: Get Midterm and Final grades from a student for any course.
#  The sum of 40% of the midterm exam grade and 60% of the final 
#  grade will give the year-end average.
#  If the average is below 50, "FAILED" will appear on the screen
#  and if it is 50 or above, "CSUCESSFUL" will be displayed on the screen. 
# This printing process is 4 lessons.
#  and the lessons will be written one after the other.

eng_res = ""
math_res = ""
his_res = ""
geo_res = ""
md_E = -1
while md_E not in range (0,100):
    md_E = float(input('Enter the student Midterm English grades'))
fl_E = -1
while fl_E not in range (0,101):
    fl_E = float(input('Enter the student English Final grades'))
if (md_E * 0.4 + fl_E *0.6) >= 50 :
    eng_res= "Passed"
else:
    eng_res= 'Failed'
md_E = -1
while md_E not in range (0,100):
    md_E = float(input('Enter the student Midterm Math grades'))
fl_E = -1
while fl_E not in range (0,101):
    fl_E = float(input('Enter the student Math Final grades'))
if (md_E * 0.4 + fl_E *0.6) >= 50 :
    math_res= "Passed"
else:
    math_res= 'Failed'
md_E = -1
while md_E not in range (0,100):
    md_E = float(input('Enter the student Midterm History grades'))
fl_E = -1
while fl_E not in range (0,101):
    fl_E = float(input('Enter the student Final History grades'))
if (md_E * 0.4 + fl_E *0.6) >= 50 :
    his_res= "Passed"
else:
    his_res= 'Failed'
md_E = -1
while md_E not in range (0,100):
    md_E = float(input('Enter the student Midterm Geography grades'))
fl_E = -1
while fl_E not in range (0,101):
    fl_E = float(input('Enter the student Final Geography grades'))
if (md_E * 0.4 + fl_E *0.6) >= 50 :
    geo_res= "Passed"
else:
    geo_res= 'Failed'
print("English Result is:",eng_res,"\nMath Result is:",math_res,"\nHistory result is:",his_res,"\nGeography Result is:",geo_res)

