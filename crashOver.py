# These two dictionaries are preloaded, you need to use them in your code
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}

alifirst = {'A': 'TONI'}
alisur = {'A': 'TESTER'}
# alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'



def alias_gen(FIRST_NAME: str, LAST_NAME: str) -> str:
    if FIRST_NAME in range(ord('A'), ord('Z')):
        return "TEST"
    return alifirst['A'] + alisur['A']

print(alias_gen(FIRST_NAME['A'], SURNAME['A']))
