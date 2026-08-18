quant_retorno = pacientes_500 = pacientes_prioridades = consulta_cara = consulta_barato = valor_consulta = tot_pacientes = 0
paciente_caro = paciente_barato = ''
pacientes = []
while True:
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    cidade = str(input('cidade: '))
    especialidade = str(input('especialidade: '))
    consulta = float(input('valor da consulta: '))
    retorno = str(input('retorno? [S/N] ')).upper()

    tot_pacientes += 1

    if retorno == 'S':
        quant_retorno += 1

    valor_consulta += consulta

    if consulta > consulta_cara:
        consulta_cara = consulta
        paciente_caro = nome

    if tot_pacientes == 1:
        consulta_barato = consulta
        paciente_barato = nome

    elif consulta < consulta_barato:
        consulta_barato = consulta
        paciente_barato = nome

    if idade >= 60:
        pacientes_prioridades += 1

    if consulta > 500:
        pacientes_500 += 1

    paciente = {'nome': nome,
                'idade': idade,
                'cidade': cidade,
                'especialidade': especialidade,
                'consulta': consulta,
                'retorno': retorno}
    pacientes.append(paciente)

    resp = input('deseja continuar? [S/N] ').upper()
    if resp == 'N':
        break

for paciente in pacientes:
    print(paciente['nome'])
    print(paciente['idade'])
    print(paciente['cidade'])
    print(paciente['especialidade'])
    print(paciente['consulta'])
    print(paciente['retorno'])

media = valor_consulta / tot_pacientes

print(f'total de pacientes: {tot_pacientes}')
print(f'valor geral das consultas: {valor_consulta}')
print(f'media do valor geral das consultas: {media}')
print(f'o paciente com a consulta mais cara foi {paciente_caro} - {consulta_cara}')
print(f'o paciente com a consulta mais barato foi {paciente_barato} - {consulta_barato}')
print(f'pacientes considerado prioridades 60+: {pacientes_prioridades}')
print(f'pacientes que pagaram mais de 500 reais em consulta: {pacientes_500}')
print(f'quantidade de pacientes que marcaram retorno: {quant_retorno}')

maior_especialidade = 0
especialidade_frequente = ''

for paciente in pacientes:
    quantidade = 0

    for outra_especialidade in pacientes:
        if paciente['especialidade'] == outra_especialidade['especialidade']:
            quantidade += 1

    if quantidade > maior_especialidade:
        maior_especialidade = quantidade
        especialidade_frequente = paciente['especialidade']

print(f'especialdades com mais pacientes: {especialidade_frequente} - {maior_especialidade}')