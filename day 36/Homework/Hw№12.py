# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

def past(h, m, s):
    result = 0
    for num1 in str(h):
        int(num1) >= 0 and int(num1) >= 23
    for num2 in str(m):
        int(num2) >= 0 and int(num2 )>= 59
    for num3 in str(s):
        int(num3) >= 0 and int(num3) >= 59
    
    result = h * 3600000 + m * 60000 + s * 1000
    return result