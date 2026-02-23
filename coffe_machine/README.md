Mini guida mentale – 5 passaggi

Apri la scatola principale (MENU)

Pensa al dizionario MENU come a una scatola gigante con dentro tutte le bevande.

Ogni chiave = nome della bevanda (espresso, latte, ecc.)

Ogni valore = un piccolo dizionario con ingredienti e costo.

Apri la scatola interna della bevanda

Ogni bevanda contiene:

"ingredients" → un altro dizionario con chiave = ingrediente, valore = quantità

"cost" → prezzo della bevanda

Questo è il secondo livello dei dizionari annidati.

Controlla le risorse

Per ogni ingrediente richiesto: confronta con quello disponibile in resources.

Usa un ciclo for ingrediente, quantità in ingredients.items().

Se manca qualcosa, ferma la preparazione e avvisa l’utente.

Gestisci il pagamento

Chiedi all’utente le monete e calcola il totale.

Confronta il totale con il costo della bevanda.

Se è sufficiente → scala le risorse, dai il resto e servi la bevanda.

Aggiorna e ripeti

Scala le risorse utilizzate.

Aggiungi il denaro al profitto.

Torna al passo 1: la macchina è pronta per la prossima bevanda.

💡 Trucchetto mentale:

Immagina scatole dentro scatole: apri una alla volta, guarda dentro, fai quello che serve, chiudi e passa alla successiva.

I cicli for servono a scorrere tutte le chiavi di ogni scatola senza perderti.