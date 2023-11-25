def nourriture():
    type = str(input("fruits ou legume : "))
    saison = str(input("hiver ou ete : "))

    if type == "fruits" and saison == "hiver":
        print("Poire, fraise, cassis")

    elif type == "fruits" and saison == "ete":
        print("orange, mandarine, kiwi")

    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")

    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")

nourriture()