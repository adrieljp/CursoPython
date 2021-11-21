#Crie uma tupla preenchida com os 20 PRIMEIROS colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A) Apenas os 5 PRIMEIROS colocados.
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabetica.
#D) Em que posição da tabela está o time da Chapecoense.
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
'São Paulo', 'Fluminense', 'Sport Recife',
'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
'Atlético-GO')
print('-=' * 25)
print(f'Os 20 primeiros colocados do Brasileirão são {times}')
print('-=' * 25)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('-=' * 25)
print(f'Os últimos 4 colocados são {times[16:]}')
print('-=' * 25)
print(f'Todos os times em ordem alfabética: {sorted(times)}')
print('-=' * 25)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print('-=' * 25)