carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))



total = sum([c[1] for c in carrinho])

print(total)

#resumindo
#print(sum(c[1] for c in carrinho]))