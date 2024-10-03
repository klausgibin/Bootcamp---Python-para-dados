# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu Nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite seu Salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite seu Bônus: "))

# 4) Calcule o valor do bônus final
bonus_final = 1000 + (salario * bonus)

# 5) Imprima cálculo do KPI para o usuário
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá, {nome} !")
print("Seu bonus foi calculado seguindo a regra: \"1000 + (salario * bonus)\"")
print(f"Seu bonus total é de R$ {bonus_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
