def contagem(s):
    count = s.upper().count('A')
    return count

string = input("Digite uma string: ")
count = contagem(string)

if count > 0:
    print(f"A letra 'a' aparece {count} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
