# create an LSH object with 2 hash functions per layer, 5 layers, and 10 buckets
lsh = LSH(k=2, L=5, n_buckets=10)

# add some vectors to the LSH object
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])
lsh.add(v1, 'item1')
lsh.add(v2, 'item2')
lsh.add(v3, 'item3')

# query for vectors that are similar to v1
similar_items = lsh.query(v1)
print(similar_items)  # should print {'item1'}
