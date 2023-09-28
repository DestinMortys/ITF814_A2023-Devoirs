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

# Exécution 1
key1 = Gen()
m1 = 0b00100011
t1 = MAC(key1, m1)

# Simulation de la transmission par Eve
m1_eve = 0b10100011  # Eve modifie le message
t1_eve = t1

# Bob vérifie le message
v1 = Verif(key1, m1_eve, t1_eve)

# Traces
print("Exécution 1:")
print("Alice: m =", bin(m1), "k =", bin(key1), "t =", bin(t1))
print("Eve: m =", bin(m1_eve), "t =", bin(t1_eve))
print("Bob: m =", bin(m1_eve), "k =", bin(key1), "t =", bin(t1_eve), "v =", v1)

# Exécution 2
key2 = Gen()
m2 = 0b10000100
t2 = MAC(key2, m2)

# Simulation de la transmission par Eve
m2_eve = 0b10000101  # Eve modifie le message
t2_eve = t2

# Bob vérifie le message
v2 = Verif(key2, m2_eve, t2_eve)

# Traces
print("\nExécution 2:")
print("Alice: m =", bin(m2), "k =", bin(key2), "t =", bin(t2))
print("Eve: m =", bin(m2_eve), "t =", bin(t2_eve))
print("Bob: m =", bin(m2_eve), "k =", bin(key2), "t =", bin(t2_eve), "v =", v2)

# Exécution 3
key3 = Gen()
m3 = 0b000110001001100010110
t3 = MAC(key3, m3)

# Simulation de la transmission par Eve
m3_eve = 0b000110001001100011110  # Eve modifie le message
t3_eve = t3

# Bob vérifie le message
v3 = Verif(key3, m3_eve, t3_eve)

# Traces
print("\nExécution 3:")
print("Alice: m =", bin(m3), "k =", bin(key3), "t =", bin(t3))
print("Eve: m =", bin(m3_eve), "t =", bin(t3_eve))
print("Bob: m =", bin(m3_eve), "k =", bin(key3), "t =", bin(t3_eve), "v =", v3)
