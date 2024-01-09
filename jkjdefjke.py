import time


start_time = time.time() #start

op_data = [] # массив - это переменная которая может принимать в себя несколько значений
test = "test"
while True:
    print(" Это приложение калькулятор")
    start = input("Если вы хотите начать работу с калькулятором введите: start "
                  " если вы хотите просмотреть историю ваших операций введите history")
    if start == "start":
        try:
            calculate = input(
                    'Список операций калькулятора: "+" - сложение \n "-" - вычитание\n "*" - умножение\n '
                    '"/"- деление\n'
                    'Введите нужную вам операцию: ')

            a = float(input('Введите первое число: '))
            b = float(input('Введите второе число: '))

            if calculate not in ('+', '-', '*', '/'):
                raise Exception("Вы ввели неккоректную операцию, введите операцию из списка")

            if calculate == '+':
                print(f'Результат вычисления: {a + b}')
                op_data.append(f"{a} + {b} = {a + b}")
            elif calculate == '-':
                print(f'Результат вычисления: {a - b}')
                op_data.append(f"{a} - {b} = {a - b}")
            elif calculate == '*':
                print(f'Результат вычисления: {a * b}')
                op_data.append(f"{a} * {b} = {a * b}")
            elif calculate == '/':
                print(f'Результат вычисления: {a / b}')
                op_data.append(f"{a} / {b} = {a / b}")
        except ZeroDivisionError:
            print("Вы не можете делить ноль!!!")
        except ValueError:
            print("Вы должны вводить цифры")
        except Exception as peremennaya:
            print(peremennaya)
        except:
            print("Неизвестная ошибка!")
    elif start == "history":
        for i in op_data:
            print(i)
    else:
        end_time = time.time()#end
        print(f"calculate worked: {round(end_time - start_time, 2)}")
        print("Приложение калькулятор завершило работу")
        break
