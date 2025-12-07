# https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    sum = 0
    for i in sheep:
        if i == True:
            sum += i
    return sum