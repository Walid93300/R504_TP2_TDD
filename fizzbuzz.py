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
    """
    Gère les 3 versions :

    - affiche()         -> Partie A, 1 à 100
    - affiche(n)        -> Partie B, 1 à n
    - affiche(n1, n2)   -> Partie C, n1 à n2
    """

    # PARTIE A — aucun argument → 1 à 100
    if len(args) == 0:
        debut, fin = 1, 100

    # PARTIE B — un argument → 1 à n
    elif len(args) == 1:
        n = args[0]
        debut, fin = 1, n

    # PARTIE C — deux arguments → n1 à n2
    elif len(args) == 2:
        debut, fin = args[0], args[1]

    else:
        raise TypeError("affiche() prend 0, 1 ou 2 arguments.")

    resultat = []
    for i in range(debut, fin + 1):
        resultat.append(_fizzbuzz_value(i))

    return "".join(resultat)


if __name__ == "__main__":
    # Exemple Partie C
    print(affiche(5, 10))
