def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n or n == 0:
        return True
    return False

numero = int(input("Digite um número: "))
if pertence_fibonacci(numero):
    print(f"Uau! O número {numero} pertence à sequência de Fibonacci :)")
else:
    print(f"Ahh... O número {numero} não pertence à sequência de Fibonacci :(")
