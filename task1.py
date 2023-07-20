# Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата


HEX_NUM = 16

def int_to_hex(num: int) -> str:
    if num == 0:
        return '0'

    hex_map = {
        0: '0', 1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'a', 11: 'b',
        12: 'c', 13: 'd', 14: 'e', 15: 'f'
    }

    hex_str = ""
    negative = False

    if num < 0:
        negative = True
        num = abs(num)

    while num > 0:
        hex_digit = num % HEX_NUM
        hex_str = hex_map[hex_digit] + hex_str
        num = num // HEX_NUM

    if negative:
        hex_str = '-' + hex_str

    return hex_str

try:
    user_number = int(input('Введите целое число: '))
    hex_user_number = int_to_hex(user_number)
    print('Шестнадцатеричное представление Вашего числа: ', hex_user_number, 'Проверка ', hex(user_number))
except ValueError:
    print('Некорректный ввод! Введите целое число')
