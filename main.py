import random
import hashlib
import re
from simhash import Simhash
from Levenshtein import distance as lev
from datasketch import MinHash

# CHATGPT minhash
def minhash(text, num_hashes=1):
  # Generate `num_hashes` random hash functions
  hashes = [hash(str(random.getrandbits(128))) for _ in range(num_hashes)]

  # Initialize minhash values to infinity
  minhash_values = [float('inf')] * num_hashes

  # Compute the minhash values for each hash function
  for word in text.split():
    for i, hash_val in enumerate(hashes):
      # Compute the hash value for the word and update the minhash if it's smaller
      minhash_values[i] = min(minhash_values[i], hash(word + str(hash_val)))

  return minhash_values


def djb2_hash(s):
  hash = 5381
  for c in s:
    hash = ((hash << 5) + hash) + ord(c)
  return hash

# Used for simhash
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]


f1 = input('Type the name of one of your uploaded files [details_1.txt]: ') or "details_1.txt"
f2 = input('Type the name of another file you uploaded [details_2.txt]: ') or "details_2.txt"

with open(f1, 'r') as f:
  # Read the contents of the file
  contents1 = f.read()
with open(f2, 'r') as f:
  # Read the contents of the file
  contents2 = f.read()
# Print hashes for examination

header = "*" * 20  # change the number to adjust the length of the header
print()
print('\nRESULTS:\n')

print('minhash')
print(f"{str(minhash(f1)[0]):<25}" + f1)
print(f"{str(minhash(f1)[0]):<25}" + f2)

print('\ndjb2:')
djb2_f1 = djb2_hash(f1)
djb2_f2 = djb2_hash(f2)
print(f"{str(djb2_f1):<25}" + f1)
print(f"{str(djb2_f2):<25}" + f2)

print('\nsimhash:')
simhash_f1 = Simhash(get_features(contents1)).value
simhash_f2 = Simhash(get_features(contents2)).value
print(f"{str(simhash_f1):<25}" + f1)
print(f"{str(simhash_f2):<25}" + f2)

print('\nmd5:')
md5_f1 = hashlib.md5(contents1.encode()).hexdigest()
md5_f2 = hashlib.md5(contents2.encode()).hexdigest()
print(md5_f1 + '\t' + f1)
print(md5_f2 + '\t' + f2)

print('\nsha256:')
sha256_f1 = hashlib.sha256(contents1.encode()).hexdigest()
sha256_f2 = hashlib.sha256(contents2.encode()).hexdigest()
print(sha256_f1 + '\t' + f1)
print(sha256_f2+ '\t' + f2)

print('\nLevenshtein Distance: ' + str(lev(contents1, contents2)))