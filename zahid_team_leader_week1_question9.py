#Question no 9

text = input('Please Enter Word')
revers_word = text[::-1]
if text == revers_word:
    print("word is a palindrome")
else:
    print("word is Not a palindrome")