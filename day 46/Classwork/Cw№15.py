lst = [1, 2, 3, 4, 5, 6]


try:
    print([i/0 for i in lst])
except TypeError:
    print("ok")
except ZeroDivisionError:
    print("cant divide by zero")
except:
    print("idk")