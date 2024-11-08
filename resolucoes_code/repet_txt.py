# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# 6 - Verificando Palíndromos 🔄

def verificar_palindromo(palavra):
    # Removendo espaços e convertendo para minúsculas para comparação correta
    palavra = palavra.replace(" ", "").lower()
    # Invertendo a palavra
    palavra_invertida = palavra[::-1]
    # Comparando a palavra original com a invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False

# Exemplo de uso
palavra = input("Digite uma palavra: ")
if verificar_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
