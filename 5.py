
string = "Hello World"
def to_alternating_case(string):
    text = string
    neu = []
    for c in text:
        if c.islower():
            a = c.upper()
            neu.append(a)
            continue
        else:
            b = c.lower()
            neu.append(b)
    ergebnis = "".join(neu)
    return ergebnis

print(to_alternating_case(string))