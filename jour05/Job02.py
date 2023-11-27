def draw_rectangle(width, height):
    # Dessiner la première ligne horizontale
    print("-" * width)

    # Dessiner les lignes verticales et horizontales internes
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Dessiner la dernière ligne horizontale
    print("-" * width)

draw_rectangle(10, 3)