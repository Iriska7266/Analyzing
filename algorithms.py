import time
import random


LEFT_EDGE = -1000
RIGHT_EDGE = 1000


def generate_int_array(left_edge: int, right_edge: int, length: int):
    """Returns random integer array of 'length' elements"""
    return [random.randint(left_edge, right_edge) for _ in range(length)]


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
