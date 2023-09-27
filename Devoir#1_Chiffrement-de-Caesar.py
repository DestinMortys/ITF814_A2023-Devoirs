# Fonction pour générer une clé aléatoire (décalage)
import random

def Gen1():
    return random.randint(0, 25)  # Le décalage est un nombre entre 0 et 25

# Fonction de chiffrement
def E1(k, m):
    ciphertext = ""
    for char in m:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            shift = k % 26  # Assurez-vous que le décalage est dans la plage de l'alphabet
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Gardez les caractères non alphabétiques inchangés
    return ciphertext

# Fonction de déchiffrement
def D1(k, c):
    return E1(-k, c)  # Déchiffrement en utilisant un décalage inverse

# Message initial
m = 'ceciestlemessageclairadechiffrer'

# Exécution des 3 Scénarios avec génération de clé aléatoire
for i in range(3):

    k = Gen1()  # Alice génère secrètement une clé aléatoire
    c = E1(k, m)  # Alice chiffre le message
    # Eve ne modifie pas le cryptogramme, donc c reste le même
    m_bob = D1(k, c)  # Bob déchiffre le message

# Affichage des résultats 
    print("\n---------------TRACE SCENARIO",i+1,"---------------")
    print(f"Alice: k={k}, c={c}")
    print(f"Eve: c={c}")
    print(f"Bob: k={k}, m={m_bob}")


