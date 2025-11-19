    # fizzbuzz.py

def _fizzbuzz_value(n: int) -> str:
    """
    Retourne la valeur correspondante à un nombre n.
    """
    if n % 15 == 0:
        return "FrisBee"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def affiche() -> str:

    resultat = []

    for n in range(1, 101):
        resultat.append(_fizzbuzz_value(n))

    # On colle tout sans espaces
    return "".join(resultat)

if __name__ == "__main__":
    # Petit test manuel si tu veux
    print(affiche())