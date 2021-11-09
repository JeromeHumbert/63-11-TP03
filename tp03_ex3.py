
def combinaison(k: int, n: int)->int:
    """
    Fonction qui va calculer le nombre de combinaisons possibles.
    :param: k: int -> Le nombre de chiffres à choisir
    :param: n: int -> Le nombre de chiffres disponibles (l'intervalle)
    :return: int -> Le nombre de combinaisons possibles.
    """
    n_factoriel = 1
    k_factoriel = 1
    n_minus_k_factoriel = 1
    for i in range(1,n):
        n_factoriel *= i
    for i in range(1,k):
        k_factoriel *= i
    for i in range(1,(n-k)):
        n_minus_k_factoriel *= i
    return int(n_factoriel/(k_factoriel*n_minus_k_factoriel))+1
