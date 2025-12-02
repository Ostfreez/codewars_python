a = 62 # "1 minute and 2 seconds")
b = 120 # "2 minutes")
c = 3662 # "1 hour, 1 minute and 2 seconds")
d = 3600 # "1 hour")
e = 15731080 # "182 days, 1 hour, 44 minutes and 40 seconds")
f = 132030240 # "4 years, 68 days, 3 hours and 4 minutes")
g = 205851834 # "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
h = 253374061 # "8 years, 12 days, 13 hours, 41 minutes and 1 second")
i = 242062374 # "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
j = 101956166 # "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
k = 33243586 # "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")
l = 0 

def format_duration(seconds):
    ergebnis = []
    if seconds == 0: return "now"
    
    minuten, seconds = divmod(seconds,60)
    stunden, minuten = divmod(minuten,60)
    tage, stunden = divmod(stunden, 24)
    jahre, tage = divmod(tage, 365)

    if jahre > 0: ergebnis.append(f"{jahre} year{'s' if jahre > 1 else ''}") 
    if tage > 0: ergebnis.append(f"{tage} day{'s' if tage > 1 else ''}") 
    if stunden > 0: ergebnis.append(f"{stunden} hour{'s' if stunden > 1 else ''}") 
    if minuten > 0: ergebnis.append(f"{minuten} minute{'s' if minuten > 1 else ''}") 
    if seconds > 0: ergebnis.append(f"{seconds} second{'s' if seconds > 1 else ''}") 
    
    if len(ergebnis) == 1: return ergebnis[0]
    else: return ', '.join(ergebnis[:-1]) + ' and ' + ergebnis[-1]

print(format_duration(a))
print(format_duration(b))
print(format_duration(c))
print(format_duration(d))
print(format_duration(e))
print(format_duration(f))
print(format_duration(g))
print(format_duration(h))
print(format_duration(i))
print(format_duration(j))
print(format_duration(k))
print(format_duration(l))