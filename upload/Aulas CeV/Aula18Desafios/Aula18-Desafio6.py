#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
#Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input().
#Mas com uma validação de dados para aceitar apenas valores que seja monetários.
from utilidadescev import dado
from moeda import resumo
preco = dado.leiadinheiro("Digite o preço: R$")
resumo(preco)