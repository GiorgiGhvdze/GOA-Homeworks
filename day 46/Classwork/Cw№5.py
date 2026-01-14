lst = ["Giorgi", 500, 90]

try:
    print(sum(lst))
except NameError:
    print("NameError")
except:
    print("Some other error")