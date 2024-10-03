# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

try:
    print("Olá, Escolha abaixo a Temperatura Atual")
    temperatura_tipo_atual = input("Digite 'C' para Celcius, 'F' para Fahre e 'K' Kelvin: ")

    temperatura_atual = float(input("Digite agora o valor da temperatura atual: "))

    print("Digite agora para qual deseja converter")
    temperatura_tipo_converter = input("'C' para Celcius, 'F' para Fahre e 'K' Kelvin: ")

    erro_conversao = False
  
    ##  CONVERSÃO DO CELCIUS  ##
    if temperatura_tipo_atual == 'C':
        if temperatura_tipo_converter == 'F':
            temperatura_convertida = temperatura_atual * 1.8 + 32 
        elif temperatura_tipo_converter =='K':
            temperatura_convertida = temperatura_atual  + 273 
        else:
            temperatura_convertida = temperatura_tipo_atual

    ##  CONVERSÃO DO FAHRE  ##
    elif temperatura_tipo_atual == 'F':
        if temperatura_tipo_converter == 'C':
            temperatura_convertida = (temperatura_atual - 32) / 1.8
        elif temperatura_tipo_converter =='K':
            temperatura_convertida = (temperatura_atual - 32) * 5/9 + 273
        else:
            temperatura_convertida = temperatura_tipo_atual
    
    ##  CONVERSÃO DO KELVIN  ##
    elif temperatura_tipo_atual == 'K':
        if temperatura_tipo_converter == 'C':
            temperatura_convertida = temperatura_atual - 273
        elif temperatura_tipo_converter =='F':
            temperatura_convertida = (temperatura_atual - 273) * 1.8 + 32
        else:
            temperatura_convertida = temperatura_tipo_atual
    else:
        erro_conversao = True


    if erro_conversao:
        print("Tipo de Temperatura Não Encontrado")
    else:
        print(f"Convertipo de {temperatura_tipo_atual} para {temperatura_tipo_converter}.")
        print(f"valor convertido: {temperatura_convertida}")

except Error as e:
	print(e)