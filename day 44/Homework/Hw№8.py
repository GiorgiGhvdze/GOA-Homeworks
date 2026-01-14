def friend(x):
    filtered = []
    for i in x:
        if len(i) == 4:
            filtered.append(i)
    return filtered