import math


def lhuns_algorithm(credit_card_number_string: str):
    # change string of number to list of number
    credit_card_number_list = list(map(int, [*credit_card_number_string]))
    even_position_numbers_list = credit_card_number_list[::2]  # starting with index 0 ,2 , 4...
    odd_position_numbers_list = credit_card_number_list[1::2]  # starting with index 1, 3, 5, 7...
    sum_of_odd = sum(odd_position_numbers_list) # sum of all numbers with odd index
    sum_of_even_operation_with_multiplication = 0
    for i in even_position_numbers_list:
        i = i*2
        sum_of_even_operation_with_multiplication += (i % 10) + (i // 10)
    total_sum = sum_of_even_operation_with_multiplication + sum_of_odd
    if total_sum % 10 == 0:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    lhuns_algorithm("4003600000000014")
    lhuns_algorithm("5610591081018250")
    lhuns_algorithm("456565765765120000000000000000")



