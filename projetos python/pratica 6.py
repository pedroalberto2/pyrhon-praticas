filme_8 = maior_nota = nota_geral = tot_filmes = media = 0
maior_filme = classificacao = ''
filmes_cadastrados = []

while True:
    titulo = str(input('titulo: '))
    genero = str(input('genero: '))
    lancamento = int(input('ano de lancamento: '))
    nota = float(input('nota: '))

    nota_geral += nota

    if nota >= maior_nota:
        maior_nota = nota
        maior_filme = titulo

    if nota <= 4:
        classificacao = 'ruim'

    elif nota <= 7:
        classificacao = 'bom'

    else:
        classificacao = 'excelente'

    filmes = [titulo, genero, lancamento, nota, classificacao]
    filmes_cadastrados.append(filmes)

    tot_filmes += 1

    if nota >= 8:
        filme_8 += 1

    resp = str(input('deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

media = nota_geral / tot_filmes

for filmes in filmes_cadastrados:
    print('-' * 30)
    print(f'titulo: {filmes[0]}')
    print(f'genero: {filmes[1]}')
    print(f'lançamento: {filmes[2]}')
    print(f'nota: {filmes[3]}')
    print(f'classificação: {filmes[4]}')
    print('-' * 30)

print(f'total de filmes cadastrados: {tot_filmes}')
print(f'media das notas: {media}')
print(f'maior nota: {maior_filme} - {maior_nota}')
print(f'filmes com nota acima de 8: {filme_8}')

print(f'filme lançados apartir de 2020: ')

for filmes in filmes_cadastrados:
    if filmes[2] >= 2020:
        print(f'- {filmes[0]}')
