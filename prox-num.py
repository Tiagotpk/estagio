# a) Sequência: 1, 3, 5, 7
sequencia = [1, 3, 5, 7]
proximo = sequencia[-1] + 2
print(f"a) Próximo número: {proximo}")

# b) Sequência: 2, 4, 8, 16, 32, 64
sequencia = [2, 4, 8, 16, 32, 64]
proximo = sequencia[-1] * 2
print(f"b) Próximo número: {proximo}")

# c) Sequência: 0, 1, 4, 9, 16, 25, 36
sequencia = [0, 1, 4, 9, 16, 25, 36]
proximo = (len(sequencia))**2
print(f"c) Próximo número: {proximo}")

# d) Sequência: 4, 16, 36, 64
sequencia = [4, 16, 36, 64]
proximo = (len(sequencia) + 2)**2
print(f"d) Próximo número: {proximo}")

# e) Sequência: 1, 1, 2, 3, 5, 8
sequencia = [1, 1, 2, 3, 5, 8]
proximo = sequencia[-1] + sequencia[-2]
print(f"e) Próximo número: {proximo}")

# f) Sequência: 2, 10, 12, 16, 17, 18, 19
sequencia = [2, 10, 12, 16, 17, 18, 19]
proximo = sequencia[-1] + 1

print(f"f) Próximo número: {proximo}")
