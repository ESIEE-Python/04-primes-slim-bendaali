"""
    Ce fichier comporte la fonction isPrime() et permet de la tester à l'aide du main.
"""


#### Fonction secondaire


def isprime(p):
    """
    Verifie si le nombre est premier.

    Args:
        Le nombre à verifier

    Returns:
        Un booleen si oui ou non le nombre est premier
    """

    if p < 2:
        return False
    for i in range(2, p):
        if (p % i) == 0:
            return False

    return True



#### Fonction principale


def main():
    """
        Permet de tester la fonction isPrime().
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
