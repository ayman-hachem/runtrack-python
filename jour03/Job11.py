def time_to_text():
    heures = int(input("heures "))
minutes = int(input("minutes "))

heures = minutes // 60
minutes_restantes = minutes % 60

if heures == 1:
        heures_texte = "1 heure"
else:
        heures_texte = f"{heures} heures"

if minutes_restantes == 1:
        minutes_texte = "1 minute"
else:
        minutes_texte = f"{minutes_restantes} minutes"

resultat = f"{heures_texte} et {minutes_texte}"
print(resultat)

