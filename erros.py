#try:
   # n1 = int(input("Digite o primeiro número: "))
    #n2 = int(input("Digite o segundo número: "))
    #resultado = n1 + n2
    #print(f"O resultado da soma é: {resultado}")
#except ValueError as error:
#    print(f"Ocorreu um erro ao tentar somar os números: {error}")

try:
    numero = float(input("Digite um número : "))
    resultado = 10 / numero
    print(f"O resultado da divisão é: {resultado}")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número válido.")