# crypto.py

def crypt(message: str, pas: int = 1) -> str:

    if pas == 0 or abs(pas) > 9:
        raise ValueError("Le pas doit être entre 1 et 9 en valeur absolue.")

    resultat = ""

    for char in message:

        # Lettres minuscules
        if 'a' <= char <= 'z':
            resultat += chr((ord(char) - ord('a') + pas) % 26 + ord('a'))

        # Lettres majuscules
        elif 'A' <= char <= 'Z':
            resultat += chr((ord(char) - ord('A') + pas) % 26 + ord('A'))

        # Caractères non alphabétiques → inchangés
        else:
            resultat += char

    # Ajout du pas en fin de message crypté
    resultat += str(pas)

    return resultat

def decrypt(message: str) -> str:

    if len(message) == 0:
        return ""

    # Récupération du pas stocké à la fin du message
    pas = int(message[-1])

    # Message crypté sans le pas final
    contenu = message[:-1]

    # Décryptage = cryptage avec un pas négatif
    return crypt(contenu, -pas)

if __name__ == "__main__":

    print("TEST MESSAGE CRYPTE :")
    print(crypt("Bonjour", 1))
    print(crypt("xyz", 2))
    print(crypt("ZOO", 3))
    print(crypt("Hello World !", 4))

    print("\nTEST MESSAGE DECRYPTE :")
    print(decrypt(crypt("Bonjour", 1)))
    print(decrypt(crypt("xyz", 2)))
    print(decrypt(crypt("ZOO", 3)))
    print(decrypt(crypt("Hello World !", 4)))