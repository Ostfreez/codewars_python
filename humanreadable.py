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
    ergebnis = 0
    if seconds == 0: ergebnis = "now"
    elif seconds == 1: ergebnis = f"{seconds} second"
    elif seconds > 1 and seconds < 60: ergebnis = f"{seconds} seconds"
    elif seconds == 60: ergebnis = "1 minute"
    elif seconds > 60 and seconds < 3600: ergebnis = f"{seconds} minuten"
        
    return ergebnis

print(format_duration(a))
print(format_duration(b))
print(format_duration(c))
# print(format_duration(d))
# print(format_duration(e))
# print(format_duration(f))
# print(format_duration(g))
# print(format_duration(h))
# print(format_duration(i))
# print(format_duration(j))
# print(format_duration(k))
print(format_duration(l))