import random  # Importiamo random per scegliere chi attacca per primo
from nemici import Zombie, Orco  # Importiamo le classi dei nemici

# Creiamo i due nemici
zombie = Zombie()
orco = Orco()

# Messaggio iniziale
print("Benvenuti nell'arena! Inizia la battaglia tra Zombie e Orco!\n")

turno = 1  # Contatore dei turni

# Ciclo principale: continua finché entrambi i nemici sono vivi
while zombie.vita > 0 and orco.vita > 0:
    print(f"--- Turno {turno} ---")
    
    # Decidiamo casualmente chi attacca per primo
    if random.choice([True, False]):
        zombie.attacca(orco)  # Zombie attacca Orco
        if orco.vita > 0:
            orco.attacca(zombie)  # Se Orco è vivo, contrattacca
    else:
        orco.attacca(zombie)  # Orco attacca Zombie
        if zombie.vita > 0:
            zombie.attacca(orco)  # Se Zombie è vivo, contrattacca
    
    # Mostriamo la vita attuale dei due nemici
    print(f"Vita attuale: Zombie = {zombie.vita}, Orco = {orco.vita}\n")
    turno += 1  # Passiamo al turno successivo

# Determiniamo il vincitore e stampiamo il risultato
vincitore = "Zombie" if zombie.vita > 0 else "Orco"
print(f"Il vincitore è: {vincitore}!")