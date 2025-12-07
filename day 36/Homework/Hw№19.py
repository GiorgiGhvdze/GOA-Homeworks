# https://www.codewars.com/kata/53dc54212259ed3d4f00071c

def sum_array(a):
    sum = 0
    for i in a:
        if len(a) > 0:
            sum += i
        elif len(a) == 0:
            return sum
    return sum