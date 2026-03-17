import random  # Importiamo il modulo random per generare danni casuali

# Classe base per tutti i nemici
class Nemico:
    def __init__(self, nome, vita, danno_min, danno_max):
        self.nome = nome            # Nome del nemico (es. Zombie, Orco)
        self.vita = vita            # Punti vita del nemico
        self.danno_min = danno_min  # Danno minimo dell'attacco
        self.danno_max = danno_max  # Danno massimo dell'attacco

    # Metodo per attaccare un avversario
    def attacca(self, avversario):
        danno = random.randint(self.danno_min, self.danno_max)  # Danno casuale tra min e max
        avversario.vita -= danno  # Sottraiamo il danno alla vita dell'avversario
        print(f"{self.nome} attacca {avversario.nome} e infligge {danno} danni!")
        # Se la vita dell'avversario scende a zero o meno, è sconfitto
        if avversario.vita <= 0:
            avversario.vita = 0
            print(f"{avversario.nome} è stato sconfitto!")

# Classe specifica per lo Zombie
class Zombie(Nemico):
    def __init__(self):
        super().__init__("Zombie", vita=50, danno_min=5, danno_max=15)

# Classe specifica per l'Orco
class Orco(Nemico):
    def __init__(self):
        super().__init__("Orco", vita=80, danno_min=10, danno_max=20)