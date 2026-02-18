import random

print("=== CARTA, FORBICE, SASSO ===")

# Scelte possibili
scelte = ["carta", "forbice", "sasso"]

# Input utente
utente = input("Scegli tra carta, forbice o sasso: ").lower()

# Controllo validità input
if utente not in scelte:
    print("Scelta non valida! Riprova.")
else:
    # Scelta computer
    computer = random.choice(scelte)
    print(f"Il computer ha scelto: {computer}")

    # Logica del gioco
    if utente == computer:
        print("Pareggio!")
    elif (utente == "carta" and computer == "sasso") or \
         (utente == "forbice" and computer == "carta") or \
         (utente == "sasso" and computer == "forbice"):
        print("Hai vinto! 🎉")
    else:
        print("Hai perso! 😢")
