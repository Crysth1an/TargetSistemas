

def applicacao():

    string = 'Olá, vamos testar para ver se funciona!'
    string_invertida = invertendo_string(string)
    output(string, string_invertida)


def invertendo_string(string):
    nova_string = ''
    for i in range(len(string) - 1, -1, -1):
        nova_string += string[i]
    return nova_string


def output(string_normal, string_invertida):
    print(string_normal)
    print(string_invertida)


if __name__ == '__main__':
    applicacao()
