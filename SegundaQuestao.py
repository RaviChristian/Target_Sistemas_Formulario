num = int(input("Digite um número inteiro: "))

# Inicializa a sequência com os dois primeiros valores
fibonacci = [0, 1]

# Gera a sequência de Fibonacci até que o último valor seja maior ou igual ao número informado
while fibonacci[-1] < num:
    # Calcula o próximo valor da sequência como a soma dos dois valores anteriores
    next_fibonacci = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fibonacci)

# Verifica se o número informado pertence à sequência de Fibonacci
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
