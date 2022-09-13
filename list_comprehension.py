string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

#lista = []
#for i in string:
#    if i == '9':
#        lista.append(string[0:10])

lista = [string[0:10] for i in string if i == '9']

#retorno = ''
#for i in range(0, len(lista)):
#    retorno += lista[i]
#    retorno += '.'

retorno = '.'.join(lista)



print(lista)
print(retorno)