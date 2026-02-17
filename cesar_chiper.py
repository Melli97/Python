def caesar_cipher(text, shift):
    # L'alfabeto in minuscolo
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""  # Qui metteremo il testo cifrato

    # Convertiamo tutto il testo in minuscolo
    text = text.lower()

    # Scorriamo ogni carattere del testo
    for char in text:
        if char in alphabet:  # Solo lettere
            # Troviamo l'indice della lettera nell'alfabeto
            index = alphabet.index(char)

            # Applichiamo lo shift e usiamo modulo 26 per "ricominciare" da a se superiamo z
            new_index = (index + shift) % 26

            # Aggiungiamo la nuova lettera al risultato
            result += alphabet[new_index]
        else:
            # Se non è una lettera (spazio, numero, simbolo), la lasciamo invariata
            result += char

    # Stampiamo il testo cifrato
    print(result)

def caesar_decipher(text, shift):
    # L'alfabeto in minuscolo
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    # Convertiamo tutto il testo in minuscolo
    text = text.lower()

    # Scorriamo ogni carattere del testo
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)

            # Shift negativo per tornare indietro
            new_index = (index - shift) % 26

            result += alphabet[new_index]
        else:
            result += char

    print(result)

caesar_cipher("aaaa", 2)