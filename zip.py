lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

total = [i[0] + i[1] for i in zip(lista_a, lista_b)]

print(total)