# Dizionario con i nomi degli studenti (chiavi)
# e i loro punteggi d'esame (valori)
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Creiamo un nuovo dizionario vuoto
# Qui salveremo i voti finali (giudizi)
student_grades = {}

# Ciclo for che scorre ogni coppia chiave-valore del dizionario
# student = nome dello studente
# score = punteggio dello studente
#.items() serve per ottenere sia la chiave che il valore di ogni elemento del dizionario.
for student, score in student_scores.items():
    
    # Se il punteggio è 91 o più
    if score >= 91:
        student_grades[student] = "Outstanding"
    
    # Se il punteggio è 81 o più (ma meno di 91,
    # perché il caso precedente è già stato controllato)
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    
    # Se il punteggio è 71 o più (ma meno di 81)
    elif score >= 71:
        student_grades[student] = "Acceptable"
    
    # Tutti gli altri casi (70 o meno)
    else:
        student_grades[student] = "Fail"

# Stampiamo il dizionario finale con i giudizi
print(student_grades)
