import hashlib

def simhash(tokens, hash_size=64):
    # Initialize an array of zeros for the hash vector
    hash_vector = [0] * hash_size

    # Iterate through each token in the input list of tokens
    for token in tokens:
        # Generate a hash value for the token
        hash_value = hashlib.md5(token.encode('utf-8')).hexdigest()

        # Convert the hash value to a binary string
        hash_bits = bin(int(hash_value, 16))[2:].zfill(128)

        # Iterate through each bit in the binary string
        for i in range(len(hash_bits)):
            # If the bit is 1, add 1 to the corresponding position in the hash vector
            if hash_bits[i] == '1':
                hash_vector[i] += 1
            # Otherwise, subtract 1 from the corresponding position in the hash vector
            else:
                hash_vector[i] -= 1

    # Generate the final hash value by setting each bit to 1 if its corresponding position in the hash vector is greater than or equal to 0, and to 0 otherwise
    simhash_value = 0
    for i in range(hash_size):
        if hash_vector[i] >= 0:
            simhash_value += 2 ** i

    return simhash_value
