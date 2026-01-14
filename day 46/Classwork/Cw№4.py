lst = ["Giorgi", 80, 90]

try:
    print(sum(listt))
except NameError:
    print("NameError")
except:
    print("Some other error")