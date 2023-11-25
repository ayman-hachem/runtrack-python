def calcul():
    num1 = int(input("Entrez le premier nombre : "))
    operator = input("Entrez l'opérateur : ")
    num2 = int(input("Entrez le deuxième nombre : "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Erreur : division par zéro")
    elif operator == "*":
        print(num1 * num2)
    elif operator == "%":
        if num2 != 0:
            print(num1 % num2)
        else:
            print("Erreur : division par zéro")
    else:
        print("Erreur : opérateur invalide")

calcul()