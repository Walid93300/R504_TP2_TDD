# crypto.py

def crypt(message: str) -> str:
  
    resultat = ""

    for char in message:
        #lettre minuscule
        if 'a' <= char <= 'z':
            #Décalage circulaire
            if char == 'z':
                resultat += 'a'
            else:
                resultat += chr(ord(char) + 1)

        #lettre majuscule
        elif 'A' <= char <= 'Z':
            if char == 'Z':
                resultat += 'A'
            else:
                resultat += chr(ord(char) + 1)

        #autres caractères (espace, chiffres, ponctuation…)
        else:
            resultat += char

    return resultat


if __name__ == "__main__":
    print(crypt("Bonjour"))
    print(crypt("xyz"))
    print(crypt("ZOO"))
    print(crypt("Hello World !"))