from utils import clear_screen
from data.data_features import load_data, save_data

history = load_data()
def start_of_the_game():
    while True:
        print("Opções de comandor")
        print("1 - Para fazer uma conta")
        print("2 - Ver histórico de contas")
        print("3 - Sair")

        comandor = int(input("Digite o comandor: "))
        if comandor == 1:
            clear_screen()
            return True
        elif comandor == 2:
            mostrar_historico()
            input("\nPressione ENTER para continuar...")
            clear_screen()
        elif comandor == 3:
            return False

def mostrar_historico():

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

    result = operators[operator](number_1, number_2)


    print('\nRealizando sua conta. Confira o resultado abaixo:')
    if isinstance(result, (int, float)):
        print(f'{number_1} {operator} {number_2} = {result:.2f}\n')
        historys.append(f'{number_1} {operator} {number_2} = {result}')
        save_data(historys)

    else:
        print(result)


