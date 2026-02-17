**Soluzione BlackJack in Python:**

Per svolgere questo esercizio ho realizzato una versione semplificata del gioco del BlackJack utilizzando Python.
Il programma simula una partita tra un giocatore e il banco, gestendo la pesca delle carte, il calcolo del punteggio e la determinazione del vincitore finale.

**Struttura :**

**Funzione per pescare una carta**
La funzione `pesca_carta()` restituisce una carta casuale scelta da una lista che rappresenta le carte del BlackJack.  
Le figure valgono 10 e l’Asso vale 11.
**Funzione per calcolare punteggio**
La funzione `calcola_punteggio(mano)` prende in input una lista di carte e restituisce la somma totale.

**Logica del gioco:**

All’inizio della partita vengono assegnate due carte al giocatore e due carte al banco.

Il giocatore può decidere se pescare un’altra carta oppure fermarsi.  
Il turno continua finché:

Il punteggio è minore o uguale a 21
Il giocatore sceglie di continuare

Se il punteggio supera 21, il giocatore perde automaticamente.

Il banco pesca carte in modo automatico finché il suo punteggio è minore di 17.

Alla fine vengono confrontati i punteggi:

Se il giocatore supera 21 → perde
Se il banco supera 21 → vince il giocatore
Se nessuno supera 21 → vince chi ha il punteggio più alto
Se i punteggi sono uguali → pareggio

**Conclusione:**
Si tratta di una versione semplificata del BlackJack, ma il gioco è funzionante e rispetta le regole richieste dalla traccia.
