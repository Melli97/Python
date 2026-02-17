import random

def pesca_carta():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calcola_punteggio(mano):
    return sum(mano)

mano_giocatore = [pesca_carta(), pesca_carta()]
mano_banco = [pesca_carta(), pesca_carta()]

punteggio_giocatore = calcola_punteggio(mano_giocatore)
punteggio_banco = calcola_punteggio(mano_banco)

# Turno del giocatore
gioco_attivo = True

while gioco_attivo:
    punteggio_giocatore = calcola_punteggio(mano_giocatore)
    
    print("\nLa tua mano:", mano_giocatore)
    print("Il tuo punteggio:", punteggio_giocatore)

    if punteggio_giocatore > 21:
        print("Hai superato 21! Hai perso")
        gioco_attivo = False
    else:
        scelta = input("Vuoi un'altra carta? (si/no): ").lower()
        
        if scelta == "si":
            mano_giocatore.append(pesca_carta())
        else:
            gioco_attivo = False

# Turno del banco
while punteggio_banco < 17:
    mano_banco.append(pesca_carta())
    punteggio_banco = calcola_punteggio(mano_banco)

print("\nMano del banco:", mano_banco)
print("Punteggio del banco:", punteggio_banco)

# Confronto punteggi
if punteggio_giocatore > 21:
    print("Hai superato 21! Hai perso")
elif punteggio_banco > 21:
    print("Il banco sballa! Hai vinto")
elif punteggio_giocatore > punteggio_banco:
    print("Hai vinto")
elif punteggio_giocatore < punteggio_banco:
    print("Hai perso")
else:
    print("Pareggio")



  