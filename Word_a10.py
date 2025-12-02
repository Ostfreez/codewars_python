s = "elephant-rides are really fun!"

def abbreviate(s):
    
    x = '-.!?'
    y = '    '
    b = s.translate(str.maketrans(x,y))
    c = b.split()
    d = []
    satz = ' ' # SEPERATOR
    for wort in c:
        if len(wort) >= 4:
            ergebnis = wort[0] + str(len(wort)-2) + wort[(len(wort)-1)] 
            d.append(ergebnis)
        else:
            d.append(wort)

    if s[-1] in x:
        d.append(s[-1])
        
    satz = satz.join(d)
    return satz    

print(abbreviate(s))