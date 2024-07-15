def input_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido.")

a = input_numero("Digite o primeiro valor: ")
b = input_numero("Digite o segundo valor: ")

soma = a + b
subtracao = a - b
multiplicacao = a * b

if b != 0:
    divisao = a / b
else:
    divisao = "Divisão por zero não é definida"

print(f"Resultado da adição: {soma}")
print(f"Resultado da subtração: {subtracao}")
print(f"Resultado da multiplicação: {multiplicacao}")
print(f"Resultado da divisão: {divisao}")
