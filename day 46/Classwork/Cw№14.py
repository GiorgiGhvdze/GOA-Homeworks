lst = [1, 2, 3, 4, 5, 6]

try:
    print(sum(str(i for i in lst)))
except TypeError:
    print("ok")