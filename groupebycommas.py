a = 1
b = 10
c = 100
d = 1000
e = 10000
f = 100000
g = 1000000
h = 35235123

def group_by_commas(n):
    #ergebnis = "{:,}".format(n)
    ergebnis = ""
    lang = len((str(n)))            
    anz_komma = (int(lang))//3
    x = str(n)
    ausgabe = x
    if anz_komma > 0:
        i = anz_komma
        while i > 0:
            ergebnis = (x[-3:] + ',' + ergebnis)
            x= x[:-3]
            i -=1
        if x: ausgabe =  x + ',' + ergebnis
        return ausgabe
    else: 
        return x

print(group_by_commas(a))
print(group_by_commas(b))
print(group_by_commas(c))
print(group_by_commas(d))
print(group_by_commas(e))
print(group_by_commas(f))
print(group_by_commas(g))
print(group_by_commas(h))



