# https://www.codewars.com/kata/5601409514fc93442500010b

def better_than_average(class_points, your_points):
    sum = 0
    for i in class_points:
        sum += i 
        sum_of_class = sum / len(class_points)
    
    if your_points > sum_of_class:
        return True
    else:
        return False