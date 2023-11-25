def calcul():
    num1 = int(input("Entrez le premier nombre : "))
    operator = input("Entrez l'opérateur : ")
    num2 = int(input("Entrez le deuxième nombre : "))

    if operator == "+":
        result = num1 + num2
        print(result)
    elif operator == "-":
        result = num1 - num2
        print(result)
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(result)
        else:
            print("Erreur : division par zéro")
            return
    elif operator == "*":
        result = num1 * num2
        print(result)
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
            print(result)
        else:
            print("Erreur : division par zéro")
            return
    else:
        print("Erreur : opérateur invalide")
        return

    if result < 0:
        print("Négatif")
    else:
        print("Positif")

calcul()