from algorithms import RIGHT_EDGE, LEFT_EDGE, generate_int_array
import time


def time_to_find_desired_number_using_sort_method(desired_number,num_list):
    start_time = time.perf_counter_ns()
    num_list.index(desired_number)
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def time_to_find_desired_number(desired_number,num_list):
    start_time = time.perf_counter_ns()
    for i in num_list:
        if i == desired_number:
            break
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def generating_list_with_desired_number (count, position_desired_number, desired_number):
    list_numbers = generate_int_array(LEFT_EDGE, RIGHT_EDGE, count)
    if position_desired_number == 'start':
        list_numbers[0] = desired_number
    elif position_desired_number == 'middle':
        list_numbers[count // 2] = desired_number
    elif position_desired_number == 'end':
        list_numbers[-1] = desired_number
    return list_numbers


def main():
    desired_number = -1
    lengths = [5, 50, 5000]
    location_desired_number = ['start', 'middle', 'end']

    for position_desired_number in location_desired_number:
        for length in lengths:
            list_numbers = generating_list_with_desired_number(length, position_desired_number, desired_number)
            find_time1 = time_to_find_desired_number(desired_number, list_numbers)
            find_time2 = time_to_find_desired_number_using_sort_method(desired_number, list_numbers)
            print(
                f'Длина {length}, положение искомого числа в списке {position_desired_number}, время поиска элемента по собственному алгоритму: {find_time1}, время поиска элемента по алгоритму "index": {find_time2}')
