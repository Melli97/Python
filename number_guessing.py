#Indovina il numero

import random

def gioca(tentativi_max):
    numero_segreto = random.randint(1, 100)
    tentativi = 0

    while tentativi < tentativi_max:
        
    #gestione errore input più sicuro
        try:
            numero_utente = int(input("Inserisci il numero: "))
        except ValueError:
            print("Devi inserire un numero!")
            continue
    #####        
        tentativi += 1
        if numero_utente > numero_segreto:
            print("Numero troppo alto")
        elif numero_utente < numero_segreto:
            print("Numero troppo basso")
        else:
            print("Hai indovinato!")
            print("Tentativi usati:", tentativi)
            return   # esce dalla funzione

    print("Hai finito i tentativi!")
    print("Il numero era:", numero_segreto)

modalita=input("Scegli la modalità: easy o hard? ").lower()
if modalita == "hard":
        gioca(5)
elif modalita == "easy":
        gioca(10)

#cond due funzioni
# def hard():
#     numero_segreto = random.randint(1, 100)
#     tentativi = 0

#     while tentativi < 5:
        
#     #gestione errore input più sicuro
#         try:
#             numero_utente = int(input("Inserisci il numero: "))
#         except ValueError:
#             print("Devi inserire un numero!")
#             continue
#     #####        
#         tentativi += 1
#         if numero_utente > numero_segreto:
#             print("Numero troppo alto")
#         elif numero_utente < numero_segreto:
#             print("Numero troppo basso")
#         else:
#             print("Hai indovinato!")
#             print("Tentativi usati:", tentativi)
#             return   # esce dalla funzione

#     print("Hai finito i tentativi!")
#     print("Il numero era:", numero_segreto)


# def easy():
#     numero_segreto = random.randint(1, 100)
#     tentativi = 0

#     while tentativi < 10:
        
#     #gestione errore input più sicuro
#         try:
#             numero_utente = int(input("Inserisci il numero: "))
#         except ValueError:
#             print("Devi inserire un numero!")
#             continue
#     #####
#         tentativi += 1
#         if numero_utente > numero_segreto:
#             print("Numero troppo alto")
#         elif numero_utente < numero_segreto:
#             print("Numero troppo basso")
#         else:
#             print("Hai indovinato!")
#             print("Tentativi usati:", tentativi)
#             return   # esce dalla funzione

#     print("Hai finito i tentativi!")
#     print("Il numero era:", numero_segreto)


  