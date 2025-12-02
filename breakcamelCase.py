a = "helloWorld"
b = "camelCase"
c = "breakCamelCase"



def solution(s):
    ergebnis = ""
    i = 0
    while i < len(s):
        if s[i].isupper():
            ergebnis = ergebnis +' ' + s[i]
        else:
            ergebnis += s[i]
        i +=1
    return ergebnis


print(solution(a))
print(solution(b))
print(solution(c))

