lst = [1,2,3,4,5,6,7,8,9,10]

evenodd = []

for i in lst:
    if i % 2 == 0:
        evenodd.append("Even")
    elif i % 2 != 0:
        evenodd.append("Odd")

print(evenodd)