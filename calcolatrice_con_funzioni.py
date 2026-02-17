# ==============================
# DEFINIZIONE DELLE FUNZIONI
# ==============================

# Funzione per sommare due numeri
def add(n1, n2):
    return n1 + n2


# Funzione per sottrarre due numeri
def subtract(n1, n2):
    return n1 - n2


# Funzione per moltiplicare due numeri
def multiply(n1, n2):
    return n1 * n2


# Funzione per dividere due numeri
def divide(n1, n2):
    # Controllo per evitare divisione per zero
    if n2 == 0:
        return "Errore: divisione per zero"
    return n1 / n2


# ==============================
# DIZIONARIO DELLE OPERAZIONI
# ==============================

# Qui colleghiamo ogni simbolo matematico
# alla funzione corrispondente
operations = {
    "+": add,         # Se l'utente sceglie "+", usa la funzione add
    "-": subtract,    # Se sceglie "-", usa subtract
    "*": multiply,    # Se sceglie "*", usa multiply
    "/": divide       # Se sceglie "/", usa divide
}


# ==============================
# PROGRAMMA PRINCIPALE
# ==============================

# Chiediamo il primo numero all'utente
# float permette numeri con la virgola (es. 3.5)
num1 = float(input("Inserisci il primo numero: "))

# Ciclo per permettere più calcoli consecutivi
while True:

    # Mostriamo le operazioni disponibili
    print("Operazioni disponibili:")
    
    # Stampiamo tutti i simboli presenti nel dizionario
    for symbol in operations:
        print(symbol)

    # L'utente sceglie quale operazione usare
    operazione = input("Scegli un'operazione: ")

    # Chiediamo il secondo numero
    num2 = float(input("Inserisci il secondo numero: "))

    # Recuperiamo la funzione corrispondente dal dizionario
    # Esempio: se operazione è "+", prende la funzione add
    funzione_calcolo = operations[operazione]

    # Eseguiamo la funzione con i due numeri
    risultato = funzione_calcolo(num1, num2)

    # Stampiamo il risultato
    print("Risultato:", risultato)

    # Chiediamo se l'utente vuole continuare
    continua = input("Vuoi continuare a calcolare con il risultato? (si/no): ")

    # Se vuole continuare, il risultato diventa il nuovo primo numero
    if continua == "si":
        num1 = risultato
    else:
        # Altrimenti usciamo dal ciclo
        print("Calcolatrice chiusa.")
        break
