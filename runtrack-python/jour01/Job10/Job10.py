montant_investissement = 5000
taux_de_rendement = 2
resultat = montant_investissement * (taux_de_rendement / 100 + 1)
total = print ("le resultat est ", resultat)

retrait = resultat * (1 - 10 / 100)
nouveau_taux_de_rendement = 1
resultat2 = retrait * (nouveau_taux_de_rendement  /100 + 1)
total2 = print("le resultat aprés retrait est ", resultat2)