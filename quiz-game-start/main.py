# Importa la classe Question dal file question_model.py
from question_model import Question
from quiz_brain import QuizBrain
# Importa la lista question_data dal file data.py
from data import question_data

# Crea una lista vuota che conterrà gli oggetti Question
question_bank = []

# Cicla attraverso ogni elemento della lista question_data
for question in question_data:
    
    # Estrae il valore associato alla chiave "text" dal dizionario
    question_text = question["text"]
    
    # Estrae il valore associato alla chiave "answer" dal dizionario
    question_answer = question["answer"]
    
    # Crea una nuova istanza della classe Question
    # passando testo e risposta al costruttore (__init__)
    new_question = Question(question_text, question_answer)
    
    # Aggiunge l'oggetto creato alla lista question_bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("Hai completato il quiz")
print(f"Il tuo punteggio finale è {quiz.score}/{quiz.question_number}")

