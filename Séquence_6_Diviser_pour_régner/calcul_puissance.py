def puissance(x: int, n: int) -> int:
    """
    Permet de calculer x exposant n
    """
    # Cas de base : si n est 0, x^0 = 1
    if n == 0:
        return 1

    # Si n est pair
    if n % 2 == 0:
        moitiee = puissance(x, n // 2)
        return moitiee * moitiee  # x^n = (x^(n/2))^2

    # Si n est impair
    else:
        return x * puissance(x, n - 1)  # x^n = x * x^(n-1)


# Tests unitaires

assert puissance(5, 25) == 298023223876953125
assert puissance(3, 3) == 27
assert puissance(44, 1) == 44
assert puissance(32, 0) == 1
