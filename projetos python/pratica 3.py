quantidade_menos_5 = produto_caro = valor_geral_estoque = quantidade_produto = 0
nome_caro = ''
estoque_geral = []

while True:
    nome = str(input('Digite o produto: '))
    estoque = int(input('quantidade de estoque: '))
    preco = int(input('preço: '))

    estoque_lista = [nome, estoque, preco]
    estoque_geral.append(estoque_lista)

    quantidade_produto += 1

    valor_estoque = estoque * preco

    valor_geral_estoque += valor_estoque

    if preco >= produto_caro:
        produto_caro = preco
        nome_caro = nome

    if estoque <= 5:
        quantidade_menos_5 += 1

    resp = str(input('quer continuar? [S/N] ')).upper()
    if resp in 'Nn':
        break

for estoque_lista in estoque_geral:
    print(f'nome: {estoque_lista[0]}')
    print(f'quantidade: {estoque_lista[1]}')
    print(f'preço: {estoque_lista[2]}')

print(f'total de produtos: {quantidade_produto}')
print(f'valor total do estoque: {valor_geral_estoque}')
print(f'produto caro: {nome_caro} - {produto_caro}')
print(f'produtos com estoque baixo: {quantidade_menos_5}')