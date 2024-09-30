import pytest
from notes import calcul_moyenne


def test_moyenne_vide():
    # Cas 1 : Liste vide
    assert calcul_moyenne([]) == 0


def test_moyenne_inf_10():
    # Cas 2 : Moyenne strictement inférieure à 10
    assert calcul_moyenne([5, 6, 8]) == pytest.approx(6.33, 0.01)


def test_moyenne_egal_10():
    # Cas 3 : Moyenne exactement égale à 10
    assert calcul_moyenne([10, 10, 10]) == 10


def test_moyenne_sup_10():
    # Cas 4 : Moyenne supérieure à 10
    assert calcul_moyenne([12, 14, 16]) == pytest.approx(14, 0.01)


if __name__ == "__main__":
    pytest.main()
