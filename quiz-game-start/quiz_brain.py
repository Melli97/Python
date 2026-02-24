class QuizBrain:
    # Classe che gestisce la logica del quiz

    def __init__(self, question_list):
        # Costruttore: viene chiamato quando si crea un oggetto QuizBrain
        # question_list è la lista delle domande passata dall'esterno
        self.question_number = 0  # Tiene traccia della domanda corrente (indice)
        self.question_list = question_list  # Salva la lista delle domande
        self.score = 0  # Inizializza il punteggio a 0

    def still_has_questions(self):
        # Controlla se ci sono ancora domande da fare
        if self.question_number < len(self.question_list):
            return True  # Ci sono ancora domande
        else:
            return False  # Non ci sono più domande

    def next_question(self):
        # Recupera la domanda corrente dalla lista
        current_question = self.question_list[self.question_number]
        
        # Incrementa il numero della domanda
        self.question_number += 1
        
        # Mostra la domanda all'utente e salva la risposta
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        
        # Controlla se la risposta è corretta
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        # Confronta la risposta dell'utente con quella corretta
        # .lower() serve per ignorare maiuscole/minuscole
        if user_answer.lower() == correct_answer.lower():
            print("giusto")
            self.score += 1  # Aumenta il punteggio se corretto
        else:
            print("Hai perso")
        
        # Mostra la risposta corretta
        print(f"La risposta corretta era: {correct_answer}")
        
        # Mostra il punteggio aggiornato
        print(f"Il tuo punteggio è {self.score}/{self.question_number}")
        
        # Riga vuota per separare le domande
        print("\n")