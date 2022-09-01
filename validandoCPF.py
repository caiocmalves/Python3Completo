cpf = int(input("Digite o CPF: "))

testecpf = str(cpf)[:-2]
cont = 10
soma = 0

for i in testecpf:
    soma += int(i) * cont
    cont -= 1

digito1 = 11 -(soma % 11)
if digito1 > 9:
    testecpf += '0'
else:
    testecpf += str(digito1)
    
cont = 11
soma = 0

for i in testecpf:
    soma += int(i) * cont
    cont -= 1

digito1 = 11 -(soma % 11)
if digito1 > 9:
    testecpf += '0'
else:
    testecpf += str(digito1)

if int(testecpf) == cpf:
    print("CPF Válido!")
else:
    print('CPF inválido!')