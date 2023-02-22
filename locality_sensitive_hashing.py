import numpy as np

class LSH:
    def __init__(self, k, L, n_buckets):
        self.k = k  # number of hash functions for each layer
        self.L = L  # number of layers
        self.n_buckets = n_buckets  # number of buckets
        self.tables = [{} for _ in range(L)]  # hash tables for each layer

    def hash(self, v):
        # returns k hash functions of v as a tuple
        rand_vectors = np.random.randn(self.k, len(v))
        projections = np.dot(rand_vectors, v)
        return tuple((projections >= 0).astype(int))

    def add(self, v, value):
        # adds an item to all hash tables
        for table in self.tables:
            hash_val = self.hash(v)
            if hash_val not in table:
                table[hash_val] = []
            table[hash_val].append(value)

    def query(self, v):
        # returns all items that hash to the same bucket as v
        candidates = set()
        for table in self.tables:
            hash_val = self.hash(v)
            if hash_val in table:
                candidates.update(table[hash_val])
        return candidates
