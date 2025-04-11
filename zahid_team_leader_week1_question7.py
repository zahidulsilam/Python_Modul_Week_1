#Question # 7
number = int(input('Please Enter Number'))
i=0
numer_calc = 0
add_number = 1
while i < number:
   final_number = numer_calc + add_number
   print(numer_calc) 
   numer_calc = add_number
   add_number = final_number
   i += 1