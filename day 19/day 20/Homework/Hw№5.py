lst = [1, "string", True]

for i in lst:
    if type(i) == str:
        print(i.upper()[-3:])