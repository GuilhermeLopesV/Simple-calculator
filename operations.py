from utils import organized_terminal
from data.data_features import load_data, save_data


history = list(load_data())
def start_of_the_game():
    while True:
        print("Opções de comandor")
        print("1 - Para fazer uma conta")
        print("2 - Ver histórico de contas")
        print("3 - Sair")

        try:
            comandor = int(input("Digite o comandor: "))
        except ValueError:
            print("Digite um número válido!\n")
            continue

        if comandor == 1:
            organized_terminal()
            return True
        elif comandor == 2:
            show_history()
            input("\nPressione ENTER para continuar...")
            organized_terminal()
        elif comandor == 3:
            return False

def show_history():

    if not history:
        print('Histórico vazio')
    else:
        for item in history:
            print(item)


def calculate(operator, number_1, number_2):
    operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else 'Não é possível dividir por zero'
            }

    if operator not in operators:
        print("Operador inválido!\n")
        return

    result = operators[operator](number_1, number_2)


    print('\nRealizando sua conta. Confira o resultado abaixo:')
    if isinstance(result, (int, float)):
        print(f'{number_1} {operator} {number_2} = {result:.2f}\n')
        history.append(f'{number_1} {operator} {number_2} = {result}')
        save_data(history)

    else:
        print(result)


