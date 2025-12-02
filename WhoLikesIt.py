def likes(names):
    x = len(names)
    if x == 0:
        return "no one likes this"
    if x == 1:
        return names[0] + " likes this"
    if x == 2:
        return names[0] + ' and ' + names[1] + " like this"
    if x == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + " like this"
    if x >= 4:
        y = x - 2
        return names[0] + ', ' + names[1] + ' and ' + str(y) + " others like this"