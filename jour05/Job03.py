def draw_triangle(height):
    for i in range(height):
        # Affiche les caractères '_' pour la ligne supérieure et inférieure du triangle
        if i == 0 or i == height - 1:
            print('_' * (2 * height - 1))
        else:
            # Affiche les caractères '\', '/' et ' ' pour les lignes intermédiaires du triangle
            line = ''
            for j in range(2 * height - 1):
                if j == height - 1 - i or j == height - 1 + i:
                    line += '/'

                else:
                    line += ' '
            print(line)

# Exemple d'utilisation avec une hauteur de 5
draw_triangle(5)