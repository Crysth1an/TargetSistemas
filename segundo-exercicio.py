def application():
    testar_numero = input_usuario()
    teste_fib = sequencia_fibonacci(testar_numero)
    if testar_numero in teste_fib:
        print(f'{testar_numero} -> pertence à sequência de Fibonacci.')
    else:
        print(f'{testar_numero} -> não pertence à sequência de Fibonacci.')


def sequencia_fibonacci(numero):
    if numero == 0:
        return [0]
    elif numero == 1:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, numero + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib


def input_usuario():
    numero = int(input("Digite um número para testarmos a sequencia de Fibonacci: "))
    return numero


if __name__ == '__main__':
    application()
