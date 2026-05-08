# Captura a entrada do usuário e realiza a conversão explícita (casting) de string para float
# para permitir cálculos com números decimais e garantir a precisão dos dados.
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Aplica a fórmula de conversão utilizando operadores aritméticos e respeitando a precedência
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Exibe o resultado final formatado utilizando f-string para uma saída clara e profissional
print(f"A temperatura convertida é {temperatura_fahrenheit} graus Fahrenheit.")
