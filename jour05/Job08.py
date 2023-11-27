def my_sort(liste):
    if len(liste) <= 1:
        return liste
    
    coups = 0
    trié = False
    
    while not trié:
        trié = True
        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                trié = False
                coups += 1
    
    print("Nombre total de coups nécessaires :", coups)
    return liste

ma_liste = [5, 2, 8, 1, 6]
liste_triee = my_sort(ma_liste)
print(liste_triee)