# map(função, iterável)
quadrados = tuple(map(lambda x: x**2, range(10)))

print(quadrados)
# (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)