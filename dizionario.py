# 🔹 Esercizio completo sui dizionari

# 1️⃣ Crea il dizionario "personaggio"
personaggio = {
    "nome": "Alba",
    "follower": 39,
    "paese": "Francia"
}

# 2️⃣ Stampa il nome e il paese
print("Nome:", personaggio["nome"])
print("Paese:", personaggio["paese"])

# 3️⃣ Aggiungi una nuova chiave "vittorie" con valore 0
personaggio["vittorie"] = 0

# 4️⃣ Aggiorna "follower" aggiungendo 50
personaggio["follower"] += 50

# 5️⃣ Cicla e stampa tutte le chiavi e i valori
print("\nDati completi del personaggio:")
for chiave, valore in personaggio.items():
    print(chiave, "->", valore)
