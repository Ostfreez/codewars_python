'''
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

'''


n1 = []                               
n2 = ["Peter"]                        
n3 = ["Jacob", "Alex"]                 
n4 = ["Max", "John", "Mark"]           
n5 = ["Alex", "Jacob", "Mark", "Max"]  

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return names[0] + ' likes this'
    if len(names) == 2:
        return names[0] + ' and ' + names[1] + ' like this'

print(likes(n1))
print(likes(n2))
print(likes(n3))