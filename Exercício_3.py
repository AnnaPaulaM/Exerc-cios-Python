q = 60                          #número de livros

preco_desc = 24.95 * 0.6        #preço com desconto em reais
custo_livros = preco_desc * q  #custo total dos livros em reais
custo_envio = 3 + (0.75)*(q-1)  #equação para calcular o custo total do envio em reais

custo_total = custo_livros + custo_envio   #custo total em reais

print('O custo total para a compra de 60 livros com desconto é de:', custo_total, 'reais.')