zahl = 8

def summation(zahl):
    i = 0
    for x in range(1, zahl+1):
        i = x + i
    return i

print(summation(zahl))