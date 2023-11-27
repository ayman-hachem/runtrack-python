def distance_marche_() :

    hauteur_marche = int(input("hauteur marche "))
    nombre_marche = int(input("nombre de marche "))
    nombre_jour = 7
    nombre_aller_jour = 5

    marche_total = (hauteur_marche / 100) * nombre_marche
    distance_semaine = nombre_aller_jour * nombre_jour * 2
    marche_m = marche_total * distance_semaine
    print(f" la personne à parcourut {marche_m} mêtres ")



distance_marche_()