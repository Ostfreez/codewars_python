'''
It took me a long time to figure out that the dictionary WORDS is provided…
'''



a = (
            ('GQEMAUVXY', ['GAME', 'PAUSE']),
            ('TDWAYZROE', ['TODAY', 'TOWER', 'TRADE', 'WATER']),
            ('EAEEAYITB', ['BEAT', 'BITE', 'BYTE']),
            ('AKUIYOOLO', ['LOOK', 'YOLK']),
            ('GVDTCAESU', ['CAGES', 'CAUSE', 'CAVES', 'DATES', 'GATES', 'GUEST', 'STAGE', 'USAGE'])
        )
print("Salat: ___________________")
print("a[0][0]: " + str(a[0][0]))           
print("a[1][0]: " + str(a[1][0]))           
print("a[2][0]: " + str(a[2][0]))           
print("a[3][0]: " + str(a[3][0]))           
print("a[4][0]: " + str(a[4][0]))           
print("liste_____________________")
print("[a][0][1]: " + str(a[0][1]))         
print("[a][1][1]: " + str(a[1][1]))         
print("[a][2][1]: " + str(a[2][1]))         
print("[a][3][1]: " + str(a[3][1]))         
print("[a][4][1]: " + str(a[4][1]))         
print("wort_____________________")
print("[a][0][1][0]: " + str(a[0][1][0]))   
print("[a][0][1][1]: " + str(a[0][1][1]))   
print("[a][1][1][0]: " + str(a[1][1][0]))   

print("len(a): " + str(len(a)))          
print("[a][0]: " + str(a[0]))               
print("[a][1]: " + str(a[1]))             

def longest_word(letters):
    # test tupel
    gesamt = letters
    erstes_ergebnis = []
    ergebnis = ()
    
    # funktion ob wort in salat
    def vergleich(salat,wort):     
        zw_ergebnis = ""
        for zeichen in wort:
            if zeichen in salat:
                zw_ergebnis += zeichen
        return zw_ergebnis
    i = 0
    l = 0
    k=0
    #print("len: " + str(len(gesamt[i][1])))
    #print(type(len(gesamt)))        
           
    while i < len(gesamt): # wenn ich hier die +1, dann bin ich bei while l < (len(gesamt[i][1])): out of range [i]
                                # wenn ich ohne +1, dann nimmt er die letzte von a nicht a[4][1] ([a][4][1]: ['CAGES', 'CAUSE', 'CAVES', 'DATES', 'GATES', 'GUEST', 'STAGE', 'USAGE'])
        while l < len(gesamt[i][1]):
            #print(vergleich(gesamt[i][0], gesamt[i][1][l]))
            zwischen = vergleich(gesamt[i][0], gesamt[i][1][l])
                    
            if zwischen == gesamt[i][1][l]:
                    erstes_ergebnis.append(zwischen)
            l += 1
        
        l = 0    
        i += 1
        #print(i)
        ergebnis += erstes_ergebnis,
        erstes_ergebnis = []
        #print(ergebnis)
    erstes_ergebnis.sort()
    return ergebnis
print(" ")
print(" ")
print("RETURN: " + str(longest_word(a)))

'''
def longest_word(letters):
    if not letters:
        return None
    
    ergebnis = []
    lang = 0

    for wort in words:
        
        temp = list(letters)
        valid = True
        for c in wort:
            if c in temp:
                temp.remove(c)
            else:
                valid = False
                break

        if valid:
            if len(wort) > lang:
                lang = len(wort)
                ergebnis = [wort]
            elif len(wort) == lang:
                ergebnis.append(wort)



    return ergebnis if ergebnis else None
'''
