a = (
            ('GQEMAUVXY', ['GAME', 'PAUSE']),
            ('TDWAYZROE', ['TRODAY', 'TOWER', 'TRADE', 'WATER']),
            ('EAEEAYITB', ['BEAT', 'BITE', 'BYTE']),
            ('AKUIYOOLO', ['LOOK', 'YOLK']),
            ('GVDTCAESU', ['CAGES', 'CAUSE', 'CAVES', 'DATES', 'GATES', 'GUEST', 'STAGE', 'USAGE'])
        )
print("Salat: ___________________")
print("a[0][0]: " + str(a[0][0]))           # TDWAYZROE
print("a[1][0]: " + str(a[1][0]))           # TDWAYZROE
print("a[2][0]: " + str(a[2][0]))           # TDWAYZROE
print("a[3][0]: " + str(a[3][0]))           # TDWAYZROE
print("a[4][0]: " + str(a[4][0]))           # TDWAYZROE
print("liste_____________________")
print("[a][0][1]: " + str(a[0][1]))         # ['TRODAY', 'TOWER', 'TRADE', 'WATER']
print("[a][1][1]: " + str(a[1][1]))         # ['TRODAY', 'TOWER', 'TRADE', 'WATER']
print("[a][2][1]: " + str(a[2][1]))         # ['TRODAY', 'TOWER', 'TRADE', 'WATER']
print("[a][3][1]: " + str(a[3][1]))         # ['TRODAY', 'TOWER', 'TRADE', 'WATER']
print("[a][4][1]: " + str(a[4][1]))         # ['TRODAY', 'TOWER', 'TRADE', 'WATER']
print("wort_____________________")
print("[a][0][1][0]: " + str(a[0][1][0]))   # GAME
print("[a][0][1][1]: " + str(a[0][1][1]))   # GAME
print("[a][1][1][0]: " + str(a[1][1][0]))   # GAME

print("len(a): " + str(len(a)))          
print("[a][0]: " + str(a[0]))               # ('GQEMAUVXY', ['GAME', 'PAUSE'])
print("[a][1]: " + str(a[1]))               # ('TDWAYZROE', ['TRODAY', 'TOWER', 'TRADE', 'WATER'])

def longest_word(letters):
    # test tupel
    gesamt = letters
    erstes_ergebnis = []
    
    # funktion ob wort in salat
    def vergleich(salat,wort):      #salat test_a[0] (a0: ('GQEMAUVXY', ['GAME']))     wort test_a[1][0] (TDWAYZROE)
        zw_ergebnis = ""
        for zeichen in wort:
            if zeichen in salat:
                zw_ergebnis += zeichen
        return zw_ergebnis
    i = 0
    k = 0
    l = 0
    print("len: " + str(len(gesamt[i][1])))
            
            #Hier muss noch eine FOR schleife über die While um denn ersten a[HIER] [fest] Variabel
            #Gucke dir die Printausgaben und positionen
            
                                # salat                         wort
    while k < len(gesamt):
        while l < (len(gesamt[i][1])):
            zwischen = vergleich(gesamt[i][0], gesamt[i][1][l])
                
            if zwischen == gesamt[i][1][l]:
                print("zwischen " + zwischen)
                erstes_ergebnis.append(zwischen)
            l += 1
            
        i += 1
        k += 1
    erstes_ergebnis.sort()
    return erstes_ergebnis

print("RETURN: " + str(longest_word(a)))

'''
Salat: ___________________
a[0][0]: GQEMAUVXY
a[1][0]: TDWAYZROE
a[2][0]: EAEEAYITB
a[3][0]: AKUIYOOLO
a[4][0]: GVDTCAESU
liste_____________________
[a][0][1]: ['GAME', 'PAUSE']
[a][1][1]: ['TRODAY', 'TOWER', 'TRADE', 'WATER']
[a][2][1]: ['BEAT', 'BITE', 'BYTE']
[a][3][1]: ['LOOK', 'YOLK']
[a][4][1]: ['CAGES', 'CAUSE', 'CAVES', 'DATES', 'GATES', 'GUEST', 'STAGE', 'USAGE']
wort_____________________
[a][0][1][0]: GAME
[a][0][1][1]: PAUSE
[a][0][1][0]: TRODAY
len(a): 5
[a][0]: ('GQEMAUVXY', ['GAME', 'PAUSE'])
[a][1]: ('TDWAYZROE', ['TRODAY', 'TOWER', 'TRADE', 'WATER'])
'''