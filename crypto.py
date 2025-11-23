# crypto.py

def crypt(message: str, pas: int = 1) -> str:

    if not (1 <= pas <= 9):
        raise ValueError("Le pas doit être un entier entre 1 et 9.")

    resultat = ""

    for char in message:

        # Lettres minuscules
        if 'a' <= char <= 'z':
            resultat += chr((ord(char) - ord('a') + pas) % 26 + ord('a'))

        # Lettres majuscules
        elif 'A' <= char <= 'Z':
            resultat += chr((ord(char) - ord('A') + pas) % 26 + ord('A'))

        # Caractères non alphabétiques
        else:
            resultat += char

    # On ajoute le pas à la fin du message crypté :
    resultat += str(pas)

    return resultat


if __name__ == "__main__":
    print(crypt("Bonjour", 1))
    print(crypt("xyz", 2))
    print(crypt("ZOO", 3))
    print(crypt("Hello World !", 4))