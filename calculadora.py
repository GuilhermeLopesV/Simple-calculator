while True:
    number_1 = input('Digite um número: ')
    number_2 = input('Digite outro número: ')
    operator = input('Digite o operador (+-/*): ')

    valid_numbers = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except ValueError:
        valid_numbers = None

    if valid_numbers is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    allowed_operators = '+-/*'

    if operator not in allowed_operators:
        print('Operador inválido.')
        continue

    if len(operator) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operator == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operator == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operator == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operator == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    close = input('Quer fechar? [s]im: ').lower().startswith('s')

    if close == 's':
        break