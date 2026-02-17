# Ciclo che va da 1 a 100 (100 incluso)
for number in range(1, 101):
    
    # Se il numero è divisibile sia per 3 che per 5
    # (prima controlliamo questo caso per evitare errori)
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    
    # Se il numero è divisibile solo per 3
    elif number % 3 == 0:
        print("Fizz")
    
    # Se il numero è divisibile solo per 5
    elif number % 5 == 0:
        print("Buzz")
    
    # Se non è divisibile né per 3 né per 5
    else:
        print(number)
