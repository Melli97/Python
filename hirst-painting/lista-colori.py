import colorgram

colori = colorgram.extract("image.jpg", 30)

lista_colori = []

for colore in colori:
    r = colore.rgb.r
    g = colore.rgb.g
    b = colore.rgb.b
    lista_colori.append((r, g, b))

print(lista_colori)