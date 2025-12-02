s = "Hello World!"

def reverse_words(s):
    x = s.split()
    ergebnis = []
    i = len(x)
    trenn = ' '
    zuruek = ''
    while i > 0:
        ergebnis.append(x[i-1])
        i = i-1
        
    for wort in ergebnis:
        zuruek = trenn.join(ergebnis)
    
    return zuruek


print(reverse_words(s))