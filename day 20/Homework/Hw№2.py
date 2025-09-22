name = input('enter ur name: ')
statement = False
for char in name: 
    if char.isupper():
        statement = True
        break

if statement:
    print(name.lower())
else:
    print(name.capitalize())