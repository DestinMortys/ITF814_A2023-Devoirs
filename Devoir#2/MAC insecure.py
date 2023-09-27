import random

# Algorithme de génération de la clé


def Gen():
    _cle = random.getrandbits(32)  # Génère 32 bits de clé aléatoire
    return _cle

# Algorithme de calcul du tag MAC


def MAC(_cle, _message):
    # Calcule le tag en faisant un XOR entre la clé et le message
    _tag = _message ^ _cle
    return _tag

# Algorithme de vérification du tag


def Verif(_cle, _message, received_tag):
    # Calcule le tag correspondant au message reçu
    tag_calcule = MAC(_cle, _message)
    # Compare les tags
    if tag_calcule == received_tag:
        return 1  # Les tags sont égaux, la vérification est réussie
    else:
        return 0  # Les tags ne sont pas égaux, la vérification a échoué


# Exemple d'utilisation
if __name__ == "__main__":
    _cle = Gen()

    # Exemple de message de 32 bits
    message = 0b10101010101010101010101010101010
    _tag = MAC(_cle, message)

    # Alice envoie le message et le tag à Bob
    # Bob reçoit le message et le tag, puis les vérifie
    resultat_verif = Verif(_cle, message, _tag)

    if resultat_verif == 1:
        print("Vérification réussie : Les tags sont égaux.")
    else:
        print("Vérification échouée : Les tags ne sont pas égaux.")
