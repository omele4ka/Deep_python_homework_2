# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions


# Поиск наибольшего общего делителя
def gcd(a:int, b:int) -> int:
    while b:
        a, b = b, a % b
    return a

# Сокращение дроби
def simplify_fraction(num, denom):
    greatest_common_divisor = gcd(num, denom)
    return num // greatest_common_divisor, denom // greatest_common_divisor

# Сложение дробей
def add_fractions(fraction1, fraction2):
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    num_sum = (num1 * denom2) + (num2 * denom1)
    denom_sum = denom1 * denom2

    return simplify_fraction(num_sum, denom_sum)

# Произведение дробей
def multiply_fractions(fraction1, fraction2):
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    num_multiplication = num1 * num2
    denom_multiplication = denom1 * denom2

    return simplify_fraction(num_multiplication, denom_multiplication)


fraction1_input = input("Введите первую дробь в формате 'a/b': ")
fraction2_input = input("Введите вторую дробь в формате 'a/b': ")

try:
    sum_result = add_fractions(fraction1_input, fraction2_input)
    multiply_result = multiply_fractions(fraction1_input, fraction2_input)
    check_sum = fractions.Fraction(fraction1_input) + fractions.Fraction(fraction2_input)
    check_multiplication = fractions.Fraction(fraction1_input) * fractions.Fraction(fraction2_input)
    print(f"Сумма дробей: {sum_result[0]}/{sum_result[1]}. Проверка: {check_sum}" )
    print(f"Произведение дробей: {multiply_result[0]}/{multiply_result[1]}. Проверка: {check_multiplication}")
except ValueError:
    print("Некорректный ввод! Введите дроби в формате 'a/b'.")
