print('~' * 60)
n = int(input('Quantos termos você quer mostrar na sua sequência FIBONACCI: '))
num_to_check = int(input('Digite um número para verificar se ele está na sequência: '))
print('~' * 60)

t1 = 0
t2 = 1
found = False

print('{} → {}'.format(t1, t2), end='')

if num_to_check == t1 or num_to_check == t2:
    found = True

c = 3
while c <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')

    if t3 == num_to_check:
        found = True

    t1 = t2
    t2 = t3
    c += 1

print(' → FIM')
print('-=-' * 20)

if found:
    print(f'O número {num_to_check} pertence à sequência de Fibonacci.')
else:
    print(f'O número {num_to_check} não pertence à sequência de Fibonacci.')


#-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

def contagem(s):
    count = s.upper().count('A')
    return count

string = input("Digite uma string: ")
count = contagem(string)

if count > 0:
    print(f"A letra 'a' aparece {count} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")


#-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f"O valor da variável SOMA ao final do processamento é {SOMA}.")

#resultado = 77

#-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

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


#-=-==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

def interruptores_lampadas():
    print("""
    1. Ligue o primeiro interruptor e deixe ligado por alguns minutos.
    2. Desligue o primeiro interruptor e ligue o segundo.
    3. Vá até a sala das lâmpadas:
       - A lâmpada que estiver acesa corresponde ao segundo interruptor.
       - A lâmpada que estiver apagada, mas quente, corresponde ao primeiro interruptor.
       - A lâmpada que estiver apagada e fria corresponde ao terceiro interruptor.
    """)
interruptores_lampadas()
