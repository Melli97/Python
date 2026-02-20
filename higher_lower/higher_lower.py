import higher_lower.game_data as game_data
import random

# Funzione che restituisce una persona casuale dalla lista
def get_random_person():
    return random.choice(game_data.data)


# Funzione principale del gioco
def higher_lower():
    score = 0             
    game_active = True     # Variabile per controllare il ciclo del gioco

    # Sceglie la prima persona casuale
    person_a = get_random_person()

   
    while game_active:

        # Sceglie una seconda persona casuale
        person_b = get_random_person()

        # Se per caso è uguale alla prima, continua a scegliere
        while person_b == person_a:
            person_b = get_random_person()

        # Mostra le due persone (senza mostrare i follower)
        print(f"A: {person_a['name']} ({person_a['country']})")
        print("VS")
        print(f"B: {person_b['name']} ({person_b['country']})")

        # Chiede all’utente chi pensa abbia più follower
        choice = input("Chi ha più follower? Scrivi A o B: ").lower()

        print("\n" * 10)

        # Salva i follower delle due persone
        followers_a = person_a["follower"]
        followers_b = person_b["follower"]

        # Determina quale risposta è corretta
        if followers_a > followers_b:
            correct_answer = "a"
        else:
            correct_answer = "b"

        # Controlla se l’utente ha risposto correttamente
        if choice == correct_answer:
            score += 1  # Aumenta il punteggio
            print(f"Corretto! Punteggio: {score}")

            # La persona B diventa la nuova A per il prossimo turno
            person_a = person_b
        else:
            # Se sbaglia, mostra i risultati e termina il gioco
            print("Sbagliato!")
            print(f"{person_a['name']} ha {followers_a} follower")
            print(f"{person_b['name']} ha {followers_b} follower")
            print(f"Punteggio finale: {score}")

            game_active = False  # Ferma il ciclo



higher_lower()

