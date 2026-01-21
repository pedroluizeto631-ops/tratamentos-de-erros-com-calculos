try:
    numero = float(input("Digite um número : "))
    resultado = 10 / numero
    print(f"O resultado da divisão é: {resultado}")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

except ValueError:

    print("Erro: Entrada inválida. Por favor, digite um número válido.")
