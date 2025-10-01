import time


def get_sorting_time(array: list[int|float]):
    """returns time needed to sort 'array'"""
    start_time = time.perf_counter_ns()
    array.sort()
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def get_summary_time(array: list[int|float]):
    """returns time needed to sum all elements of 'array'"""
    start_time = time.perf_counter_ns()
    sum(array)
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def get_square_time(array: list[int|float]):
    """returns time needed to square every element of 'array'"""
    start_time = time.perf_counter_ns()
    for i in range(len(array)):
        array[i] *= array[i]
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def get_bubble_sort_time(array: list[int|float]):
    """returns time of ordinary bubble sorting execution time"""
    start_time = time.perf_counter_ns()
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    finish_time = time.perf_counter_ns()
    return finish_time - start_time
