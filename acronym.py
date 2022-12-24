user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
b=" "
for i in text:
    a = a+str(i[0]).upper()
    b = b+str(i[3]).upper()
print(a)
print(b)
