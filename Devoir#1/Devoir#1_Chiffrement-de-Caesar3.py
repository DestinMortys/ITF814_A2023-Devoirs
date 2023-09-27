import random

# Fonction pour générer une clé secrète k de longueur 32
def Gen3():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(32))

# Fonction de chiffrement de César de longueur 32
def E3(k, m):
    if len(k) != 32:
        raise ValueError("La clé doit avoir une longueur de 32 caractères")
    
    ciphertext = ""
    for i in range(len(m)):
        if m[i].isalpha():
            shift = ord(k[i]) - ord('a')
            if m[i].islower():
                new_char = chr(((ord(m[i]) - ord('a') + shift) % 26) + ord('a'))
            else:
                new_char = chr(((ord(m[i]) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += new_char
        else:
            ciphertext += m[i]
    return ciphertext

# Fonction de déchiffrement de César de longueur 32
def D3(k, c):
    if len(k) != 32:
        raise ValueError("La clé doit avoir une longueur de 32 caractères")
    
    plaintext = ""
    for i in range(len(c)):
        if c[i].isalpha():
            shift = ord(k[i]) - ord('a')
            if c[i].islower():
                new_char = chr(((ord(c[i]) - ord('a') - shift) % 26) + ord('a'))
            else:
                new_char = chr(((ord(c[i]) - ord('A') - shift) % 26) + ord('A'))
            plaintext += new_char
        else:
            plaintext += c[i]
    return plaintext

# Message initial 
message = 'ceciestlemessageclairadechiffrer'

# Exécution des 3 Scénarios avec génération de clé aléatoire
for i in range(3):
    key = Gen3()  # Alice génère une clé secrète
    ciphertext = E3(key, message)  # Alice chiffre le message
    # Eve ne modifie pas le cryptogramme, donc ciphertext reste le même
    plaintext = D3(key, ciphertext)  # Bob déchiffre le message

    # Affichage des résultats
    print("\n---------------TRACE SCENARIO",i+1,"---------------")
    print(f"Alice: k={key}, m={message}")
    print(f"Eve: c={ciphertext}")
    print(f"Bob: k={key}, m={plaintext}")
