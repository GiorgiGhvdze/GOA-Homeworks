# https://www.codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    nums = ""
    for i in x:
        if int(i) < 5:
            nums += "0"
        elif int(i) >= 5:
            nums += "1"
    return nums