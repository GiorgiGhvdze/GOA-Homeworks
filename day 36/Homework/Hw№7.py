# https://www.codewars.com/kata/57f780909f7e8e3183000078

def grow(arr):
    multiply = 1
    
    for i in arr:
        multiply = multiply * i
    return multiply
        