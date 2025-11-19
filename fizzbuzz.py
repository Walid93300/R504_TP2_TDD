# fizzbuzz.py

def _fizzbuzz_value(n: int) -> str:
    if n % 15 == 0:
        return "FrisBee"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def affiche(*args) -> str:
    # Partie A : aucun argument → 1 à 100
    if len(args) == 0:
        debut, fin = 1, 100
    
    # Partie B : un argument → 1 à n
    elif len(args) == 1:
        n = args[0]
        debut, fin = 1, n
    
    else:
        raise TypeError("affiche() prend 0 ou 1 argument pour l'instant.")

    resultat = []
    for i in range(debut, fin + 1):
        resultat.append(_fizzbuzz_value(i))

    return "".join(resultat)

if __name__ == "__main__":
    print(affiche(15))
