import random  # Serve per scegliere una parola casuale

# Lista delle parole possibili
parole = ["python", "computer", "programmazione", "gioco", "sviluppatore"]

# Il computer sceglie una parola casuale dalla lista
parola = random.choice(parole)

# Lista che conterrà le lettere indovinate dall'utente
lettere_indovinate = []

# Numero massimo di errori consentiti
tentativi = 6

print("=== GIOCO DELL'IMPICCATO ===")

# Il gioco continua finché ci sono tentativi disponibili
while tentativi > 0:
    
    parola_nascosta = ""  # Stringa che mostra la parola con lettere scoperte e trattini

    # Costruisce la parola visibile all'utente
    for lettera in parola:
        # Se la lettera è stata indovinata, la mostra
        if lettera in lettere_indovinate:
            parola_nascosta += lettera + " "
        else:
            # Altrimenti mostra un trattino
            parola_nascosta += "_ "

    # Mostra la parola aggiornata
    print("\nParola:", parola_nascosta)

    # Se non ci sono più trattini, significa che l'utente ha vinto
    if "_" not in parola_nascosta:
        print("Complimenti! Hai vinto!")
        break  # Esce dal ciclo

    # Chiede una lettera all'utente
    scelta = input("Scegli una lettera: ").lower()

    # Controlla che l'input sia valido (una sola lettera)
    if len(scelta) != 1 or not scelta.isalpha():
        print("Inserisci una sola lettera valida.")
        continue  # Torna all'inizio del ciclo

    # Controlla se la lettera è già stata scelta
    if scelta in lettere_indovinate:
        print("Hai già scelto questa lettera.")
        continue

    # Aggiunge la lettera alla lista delle lettere provate
    lettere_indovinate.append(scelta)

    # Se la lettera NON è nella parola
    if scelta not in parola:
        tentativi -= 1  # Riduce i tentativi
        print(f"Sbagliato! Tentativi rimasti: {tentativi}")
    else:
        print("Bravo! Lettera corretta!")

# Se i tentativi arrivano a 0, il giocatore perde
if tentativi == 0:
    print(f"Hai perso! La parola era: {parola}")
