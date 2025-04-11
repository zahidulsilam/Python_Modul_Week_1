#Question no 8

text = input('Please Enter Word')
tlen = len(text) - 1
new_text = ''
for i in range(tlen, -1, -1):
    new_text = new_text+text[i]
print(new_text)  