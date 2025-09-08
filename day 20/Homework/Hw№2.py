name = input('Enter ur name: ')

for i in name: 
    if i == i.upper():
        print(name.lower())
    else:
        print(name.capitalize())
    break