import random

# Fonction pour générer une clé secrète k (masque jetable)
def Gen2(message_length):
    return ''.join(random.choice('01') for _ in range(message_length))

# Fonction de chiffrement
def E2(k, m):
    if len(k) != len(m):
        raise ValueError("La clé et le message doivent avoir la même longueur")
    
    ciphertext = ""
    for i in range(len(m)):
        encrypted_bit = str(int(k[i]) ^ int(m[i]))  # XOR entre la clé et le message
        ciphertext += encrypted_bit
    return ciphertext

# Fonction de déchiffrement
def D2(k, c):
    if len(k) != len(c):
        raise ValueError("La clé et le cryptogramme doivent avoir la même longueur")
    
    plaintext = ""
    for i in range(len(c)):
        decrypted_bit = str(int(k[i]) ^ int(c[i]))  # XOR entre la clé et le cryptogramme
        plaintext += decrypted_bit
    return plaintext

# Message initial
message = 'ceciestlemessageclairadechiffrer'

# Convertir le message en bits
message_bits = ''.join(format(ord(char), '08b') for char in message)

##########Exécution des 3 Scenarios d'exécution###############
for i in range(3):

    key = Gen2(len(message_bits))  # Alice génère une clé secrète
    ciphertext = E2(key, message_bits)  # Alice chiffre le message
    # Eve ne modifie pas le cryptogramme, donc ciphertext reste le même
    plaintext_bits = D2(key, ciphertext)  # Bob déchiffre le message en bits
    plaintext = ''.join(chr(int(plaintext_bits[i:i+8], 2)) for i in range(0, len(plaintext_bits), 8))  # Conversion en texte

    # Affichage des résultats
    print("\n---------------TRACE SCENARIO",i+1,"---------------")
    print(f"Alice: k={key}, m={message_bits}")
    print(f"Eve: c={ciphertext}")
    print(f"Bob: k={key}, m={plaintext_bits}, \n plaintext={plaintext}")

