import random

def generate_private_key(n):
    """
    Generate a private key for knapsack encryption with n bits
    """
    private_key = []
    total = 0
    while total < 2**n:
        next_value = random.randint(total+1, total*2)
        private_key.append(next_value)
        total += next_value
    return private_key

def generate_public_key(private_key, m, n):
    """
    Generate a public key for knapsack encryption with the given private key and multiplier m
    """
    public_key = [(m*x) % n for x in private_key]
    return public_key

def encrypt(plaintext, public_key):
    """
    Encrypt the given plaintext using the given public key
    """
    ciphertext = sum(plaintext[i]*public_key[i] for i in range(len(plaintext)))
    return ciphertext

def decrypt(ciphertext, private_key, m, n):
    """
    Decrypt the given ciphertext using the given private key and multiplier m
    """
    inverse_m = pow(m, -1, n)
    knapsack_sum = ciphertext * inverse_m % n
    knapsack = []
    for value in reversed(private_key):
        if knapsack_sum >= value:
            knapsack.append(1)
            knapsack_sum -= value
        else:
            knapsack.append(0)
    plaintext = [knapsack[i] for i in reversed(range(len(knapsack)))]
    return plaintext

private_key = generate_private_key(8)

public_key = generate_public_key(private_key, 5, 257)

plaintext = [8, 5, 12, 12, 15]
ciphertext = encrypt(plaintext, public_key)

decrypted_plaintext = decrypt(ciphertext, private_key, 5, 257)
assert decrypted_plaintext == plaintext