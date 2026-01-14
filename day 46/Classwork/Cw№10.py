age = 9

try:
    print(age / 0)
except ZeroDivisionError:
    print("YOU CANT DIVIDE BY 0")