# A função input() lê a entrada do usuário como string; o int() realiza a conversão explícita (casting) para número inteiro
numero_escolhido = int(input("Digite um número inteiro entre 1 e 10: "))

# Processamento do cálculo utilizando a biblioteca math com variável autodescritiva
resultado_fatorial = math.factorial(numero_escolhido)

# Exibição do resultado final utilizando f-string para maior clareza
print(f"O fatorial de {numero_escolhido} é de: {resultado_fatorial}")
