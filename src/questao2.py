def fibonacci_ate(numero):
    
    #primeiros valores
    sequencia = [0, 1]

    #montar a sequencia até o ultimo valor ser maior ou igual ao numero
    while sequencia[-1] < numero:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)

    return sequencia

def pertence_a_fibonacci(numero):

    #montar a sequência até o número
    sequencia = fibonacci_ate(numero)

    return numero in sequencia

def main():

    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if pertence_a_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()