
stops = 2
descending = [0,2,4,4]
onboarding = [3,5,2,0]
# ergebnis soll sein  6


def tram(stops, descending, onboarding):
    x = 0
    y = 0
    for stelle in range(stops):
        x -= descending[stelle]
        x += onboarding[stelle]
        if x > y:
            y = x
        else:
            continue
        print(stelle)
    return y

print(tram(stops, descending, onboarding))