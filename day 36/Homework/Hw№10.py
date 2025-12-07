# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c

def find_needle(haystack):
    
    for i in haystack:
        needle =  haystack.index("needle")
        return "found the needle at position " + str(needle)