# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrev_name(name):
    surname = name.find(" ")
    
    return (name[0].upper() + "." + name[surname+1].upper())