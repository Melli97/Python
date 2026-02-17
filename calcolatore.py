def calculate_love_score(name1, name2):
    
    # Uniamo i due nomi in un'unica stringa
    # e trasformiamo tutto in minuscolo
    # così non ci sono problemi tra maiuscole e minuscole
    combined_names = (name1 + name2).lower()

    
    # Contiamo quante volte compare ogni lettera
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    
    # Sommiamo tutte le occorrenze
    true_total = t + r + u + e
    
    # Contiamo le lettere di LOVE
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e2 = combined_names.count("e")  # la e si conta di nuovo
    
    # Sommiamo tutte le occorrenze
    love_total = l + o + v + e2
    
    # Uniamo i due risultati come stringa
    # esempio: 5 e 3 → "5" + "3" = "53"
    love_score = int(str(true_total) + str(love_total))
    
    # Stampiamo il risultato finale
    print(love_score)

calculate_love_score("Marcello","Antonella")