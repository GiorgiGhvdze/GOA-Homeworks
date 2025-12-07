# https://www.codewars.com/kata/5583090cbe83f4fd8c000051

def digitize(n):
    nums = []
    for i in str(n)[::-1]:
        nums.append(int(i))
    return nums