nom = str(input("nom du produit "))
prix_unitaire = float(input(" prix unitaire "))
quantité = int(input("quantité "))
total = (prix_unitaire * quantité) * 10 / 100
print(f"Le total est de {total}\u20AC")


