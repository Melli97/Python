# Creiamo un dizionario vuoto per salvare le offerte
asta = {}

# Ciclo infinito per aggiungere offerte
while True:

    # Chiediamo all'utente il nome dell'offerente
    nome = input("Nome? ")

    # Chiediamo all'utente il prezzo e lo convertiamo in intero
    prezzo = int(input("prezzo? "))

    # Salviamo l'offerta nel dizionario
    # La chiave è il nome, il valore è il prezzo
    asta[nome] = prezzo

    # Chiediamo se vogliono inserire un'altra offerta
    continua = input("Vuoi aggiungere un'altra offerta? (si/no) ")

    # Stampa alcune righe vuote per "pulire" lo schermo
    print("\n" * 10)

    # Se l'utente risponde "no", interrompiamo il ciclo
    if continua == "no":
        break

# ------------------------------------------------------------
# METODO COMMENTATO CON CICLO MANUALE (non usato)
# massimo = 0           # variabile per salvare il prezzo più alto
# vincitore = ""        # variabile per salvare il nome del vincitore
# for nome, prezzo in asta.items():
#     if prezzo > massimo:
#         massimo = prezzo
#         vincitore = nome
# ------------------------------------------------------------

# Trova il vincitore usando la funzione max()
# max(asta, key=asta.get) significa:
# "prendi la chiave con il valore più alto nel dizionario"
vincitore = max(asta, key=asta.get)

# Il prezzo massimo corrispondente al vincitore
massimo = asta[vincitore]

# Stampiamo il prezzo massimo
print("Il prezzo massimo è", massimo)

# Stampiamo chi ha vinto e il prezzo dell'offerta
print("Il vincitore è", vincitore, "con il prezzo di", massimo)

# Stampiamo l'intero dizionario con tutte le offerte
print(asta)
