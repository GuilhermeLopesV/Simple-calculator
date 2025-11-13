def calculator():
     while True:
        try:
            number_1 = float(input('Digite um número: '))
            operator = input('Digite o operador (+-/*): ').strip()
            number_2 = float(input('Digite outro número: '))
        except ValueError:
            print('Um ou ambos os números digitados são inválidos.\n')
            continue

        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else 'Não é possível dividir por zero'
        }

        if operator not in operators:
            print('Operador inválido.')
            continue

        result = operators[operator](number_1, number_2)

        print('\nRealizando sua conta. Confira o resultado abaixo:')
        if isinstance(result, (int, float)):
            print(f'{number_1} {operator} {number_2} = {result:.2f}\n')
        else:
            print(result)

        close = input('Quer fechar? [s]im ou [n]ão: ').strip().lower()

        if close == 's':
            print('Fechando a calculadora...')
            break

calculator()