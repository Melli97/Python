# 1️⃣ Primo livello: chiavi principali (es. "latte", "espresso")  
#    → Operazione: scegli la bevanda, prendi il dizionario corrispondente  

# 2️⃣ Secondo livello: dizionario interno (es. {"ingredients": {...}, "cost": ...})  
#    → Operazione: accedi agli ingredienti o al costo della bevanda  

# 3️⃣ Terzo livello: dizionario ingredients (es. water: 200, milk:150, coffee:24)  
#    → Operazione: ciclo for su chiavi e valori → controlli e scalai le risorse (altro dizionario)

# 4️⃣ Ciclo for combinato:  
#    → Primo for: scorre le bevande  
#    → Secondo for: scorre gli ingredienti di ciascuna bevanda  
#    → Operazioni: confronto quantità, sottrazione dalle resources, preparazione bevanda

# 
# Risorse iniziali della macchina
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Menu con ingredienti richiesti e costo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
machine_on = True

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

while machine_on:

    scelta = input("Che cosa desideri? (espresso, latte, cappuccino): ").lower()

    if scelta == "off":
        machine_on = False

    elif scelta == "report":
        print_report()

    elif scelta in MENU:

        bevanda = MENU[scelta]
        ingredienti = bevanda["ingredients"]

        # Controllo risorse
        risorse_sufficienti = True

        for ingrediente in ingredienti:
            if resources[ingrediente] < ingredienti[ingrediente]:
                print(f"Non c'è abbastanza {ingrediente}!")
                risorse_sufficienti = False

        if risorse_sufficienti:

            # Inserimento monete
            costo = bevanda["cost"]

            quarters = int(input("Quanti quarters? "))
            dimes = int(input("Quanti dimes? "))
            nickels = int(input("Quanti nickels? "))
            pennies = int(input("Quanti pennies? "))

            totale = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            totale = round(totale, 2)

            # Controllo pagamento
            if totale < costo:
                print("Soldi insufficienti. Rimborso.")
            else:
                resto = round(totale - costo, 2)
                if resto > 0:
                    print(f"Ecco ${resto} di resto.")

                # Aggiorna profitto
                profit += costo

                # Scala risorse
                for ingrediente in ingredienti:
                    resources[ingrediente] -= ingredienti[ingrediente]

                print(f"Ecco la tua {scelta}. Goditi la bevanda!")

    else:
        print("Scelta non valida.")


