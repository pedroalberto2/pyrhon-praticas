livros_2020 = livro_70 = livro_maior = livro_menor = valor_geral = tot_livros = 0
classificacao = nome_maior = nome_menor = ''
livros = []

while True:
    titulo = str(input('titulo: '))
    autor = str(input('autor: '))
    genero = str(input('genero: '))
    ano = int(input('ano: '))
    preco = float(input('preço: '))

    if preco <= 30:
        classificacao = 'barato'

    elif preco <= 70:
        classificacao = 'moderado'

    else:
        classificacao = 'caro'

    tot_livros += 1

    valor_geral += preco

    if preco > livro_maior:
        livro_maior = preco
        nome_maior = titulo

    if tot_livros == 1:
        livro_menor = preco
        nome_menor = titulo

    elif preco < livro_menor:
        livro_menor = preco
        nome_menor = titulo

    if preco > 70:
        livro_70 += 1

    if ano >= 2020:
        livros_2020 += 1

    livro = {
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'ano': ano,
        'preço': preco,
        'classificação': classificacao}
    livros.append(livro)

    resp = str(input('deseja continuar? [S/N] ')).upper()
    if resp in 'N':
        break

media = valor_geral / tot_livros

for livro in livros:
    print('-' * 30)
    print(livro['titulo'])
    print(livro['autor'])
    print(livro['genero'])
    print(livro['ano'])
    print(livro['preço'])
    print(livro['classificação'])
    print('-' * 30)

print(f'total de livros: {tot_livros}')
print(f'valor geral dos livros: {valor_geral:.2f}')
print(f'media geral dos livros: {media:.2f}')
print(f'livro mais caro: {nome_maior} - {livro_maior}')
print(f'livro mais barato: {nome_menor} - {livro_menor}')
print(f'livros que custam mais de 70R$: {livro_70}')
print(f'livros que foram publicado de 2020 adiante: {livros_2020}')