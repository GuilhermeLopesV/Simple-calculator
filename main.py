from operations import calculate, start_of_the_game
from utils import start

def calculator():
    while True:
        if not start_of_the_game():
            print("Encerrando o programa...")
            break

        try:
            number_1 = float(input('Digite um número: '))
            operator = input('Digite o operador (+-/*): ').strip()
            number_2 = float(input('Digite outro número: '))
        except ValueError:
            print('Entrada inválida!\n')
            continue

        calculate(operator, number_1, number_2)

if __name__ == "__main__":
    start()
    calculator()
