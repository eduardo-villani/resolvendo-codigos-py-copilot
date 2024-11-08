# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# 3 - Operações Matemáticas Simples 📐
def calcular(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")

resultado = calcular(num1, num2, operacao)
print(f"Resultado: {resultado}")


# 4 - Verificando Números Pares e Ímpares 🧮

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Exemplo de uso
numero = int(input("Digite um número inteiro: "))
resultado = verificar_par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")


# 5 - Calculando Média de Notas 📚
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

# Exemplo de uso
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)
print(f"A média das notas é: {media}")

