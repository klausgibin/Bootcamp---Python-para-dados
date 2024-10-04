### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# qtd = [30,40,40,10,-10]
# preco = [-10,40,0,10,-10]



# for i in range(0,len(qtd)):
#     print(f"'qtd': {qtd[i]}")
#     print(f"'preco': {preco[i]}")

#     if qtd[i] > 0 and preco[i] > 0 :
#         print("Dados Valdios")
#         print("--------------")
#     else:
#         print("Dados Inválidos")
#         print("--------------")



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# logs = {'1': {'timestamp': '2021-06-23 10:00:00', 'level': 'OK', 'message': 'Sem Erros'},
# '2': {'timestamp': '2021-06-23 11:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
# '3': {'timestamp': '2021-06-23 12:00:00', 'level': 'ERROR', 'message': 'Falha na Rede'},
# '4': {'timestamp': '2021-06-23 10:00:00', 'level': 'OK', 'message': 'Sem Erros'}}

# error_logs = {}

# for key, value in logs.items():
#     if value['level'] == 'ERROR':
#         error_logs[key] = value

# ## Imprimindo os Logs com Erros
# print("Logs com nível ERROR")
# print("--------------------")
# print()
# for key, value in error_logs.items():
#     print(f"Chave: {key}")
#     print(f"Data: {value['timestamp']}")
#     print(f"Level: {value['level']}")
#     print(f"Mensagem: {value['message']}")
#     print("--------------------")
#     print()


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

import re

inf_user = {'idade':'19','email':'####@gmail.com'}

idade_valida = False
email_valido = False

# Validação Range de Idade
IDADE_MIN = 18
IDADE_MAX = 65

if int(inf_user['idade']) >= IDADE_MIN and int(inf_user['idade']) <= IDADE_MAX:
    idade_valida = True

#Validação E-mail
padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email_valido = re.match(padrao_email,inf_user['email']) is not None

if idade_valida and email_valido:
    print("Dados de usuário válidos")
elif not idade_valida:
    print("Idade não está entre 18 e 65 anos")
else:    
    print("E-mail Inválido")



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# texto = "era uma vez uma casa de campo, esta casa era bem pequena e uma vez caiu."

# palavras = texto.split() # Quebrando o texto pelo espaço, delimitador padrao
# contagem = {}

# for palavra in palavras:
#     if palavra in contagem:
#         contagem[palavra] += 1
#     else:
#         contagem[palavra] = 1

# for palavra, count in contagem.items():
#     print(f"'{palavra}': {count}")

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.