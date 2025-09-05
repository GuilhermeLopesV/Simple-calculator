while True:
    try:
        number_1 = input('Digite um número: ')
        operator = input('Digite o operador (+-/*): ')
        number_2 = input('Digite outro número: ')
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except ValueError:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    except ZeroDivisionError:
        print('Não é possível dividir por zero.')
        continue

    allowed_operators = '+-/*'
    soma = num_2_float + num_1_float
    subtracao = num_2_float - num_1_float
    multiplicacao = num_2_float * num_1_float
    divisao = num_1_float / num_2_float

    if operator not in allowed_operators:
        print('Operador inválido.')
        continue

    if len(operator) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operator == '+':
        print(f'{num_1_float}+{num_2_float}=', soma)
    elif operator == '-':
        print(f'{num_1_float}-{num_2_float}=', subtracao)
    elif operator == '/':
        print(f'{num_1_float}/{num_2_float}=', f'{divisao:.2f}')
    elif operator == '*':
        print(f'{num_1_float}*{num_2_float}=', multiplicacao)
    else:
        print('Nunca deveria chegar aqui.')

    close = input('Quer fechar? [s]im ou [n]ão: ').lower()

    if close == 's':
        print('Fechando a calculadora.')
        break