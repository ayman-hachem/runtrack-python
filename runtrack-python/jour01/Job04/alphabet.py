import string

def listAlphabet():
    return list(string.ascii_lowercase)


print(listAlphabet())
print()
liste_reverse = list(reversed(listAlphabet()))
print(liste_reverse)