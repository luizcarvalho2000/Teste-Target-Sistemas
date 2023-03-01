""" No exemplo de uso apresentado, chamamos a função verifica_fibonacci com o argumento 8.
 Isso significa que o programa irá calcular a sequência de Fibonacci até o número 8 e
verificar se 8 pertence à sequência. Como 8 é um número da sequência (8 = 0 + 1 + 1 + 2 + 3 + 5),
 o programa irá imprimir a mensagem "8 pertence à sequência de Fibonacci!"."""
def fibonacci(n):
    """Função que retorna a sequência de Fibonacci até o número n"""
    fib = [0, 1]  # Inicia a sequência com os valores 0 e 1
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])  # Adiciona o próximo valor na sequência
    return fib

def verifica_fibonacci(n):
    """Função que verifica se um número pertence à sequência de Fibonacci"""
    fib = fibonacci(n)
    if n in fib:
        print(f"{n} pertence à sequência de Fibonacci!")
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")

# Exemplo de uso
verifica_fibonacci(8)


