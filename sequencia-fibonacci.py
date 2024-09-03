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
