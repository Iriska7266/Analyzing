import random
import matplotlib
import matplotlib.pyplot
import time
import math

LEFT_EDGE = -1000
RIGHT_EDGE = 1000


def generate_int_array(length: int):
    """Returns random integer array of 'length' elements"""
    return [random.randint(LEFT_EDGE, RIGHT_EDGE) for _ in range(length)]


def get_sorting_time(array: list[int]):
    """returns time needed to sort 'array'"""
    start_time = time.perf_counter_ns()
    array.sort()
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def get_summary_time(array: list[int]):
    """returns time needed to sum all elements of 'array'"""
    start_time = time.perf_counter_ns()
    sum(array)
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def get_square_time(array: list[int]):
    """returns time needed to square every element of 'array'"""
    start_time = time.perf_counter_ns()
    for i in range(len(array)):
        array[i] *= array[i]
    finish_time = time.perf_counter_ns()
    return finish_time - start_time


def draw_execution_time(n, samples_sorting, samples_summary, samples_square,):
    matplotlib.pyplot.plot(n, samples_sorting, label="Sorting")
    matplotlib.pyplot.plot(n, samples_summary, label="Summary")
    matplotlib.pyplot.plot(n, samples_square, label="Square")

    matplotlib.pyplot.legend()
    matplotlib.pyplot.title("Execution time")
    matplotlib.pyplot.xlabel("Count of numbers")
    matplotlib.pyplot.ylabel("Time, ns")

    matplotlib.pyplot.show()


def draw_compare_for_sorting(n, sort_time):
    """Common sort function has O(n*log(n)) difficulty"""
    matplotlib.pyplot.plot(n, sort_time, label="Fact time")

    y = [i * math.log2(i) for i in n]
    matplotlib.pyplot.plot(n, y, label="Expecting time")

    matplotlib.pyplot.title("1. Sorting algorithm")
    matplotlib.pyplot.xlabel("Count of numbers")
    matplotlib.pyplot.ylabel("Time, ns")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()


def part_1():
    n = [10000, 11000, 12000, 13000, 50000]
    #n = [1, 2, 5, 7, 10, 15, 20, 30, 50, 70, 100, 150, 200]

    samples_sorting = []
    samples_summary = []
    samples_square = []

    # Getting time of every algorithm execution with different counts of numbers
    for count in n:
        numbers = generate_int_array(count)

        # Измеряем каждую операцию
        time_sort = get_sorting_time(numbers)
        time_sum = get_summary_time(numbers)
        time_square = get_square_time(numbers)

        samples_sorting.append(time_sort)
        samples_summary.append(time_sum)
        samples_square.append(time_square)

    #draw_execution_time(n, samples_sorting, samples_summary, samples_square)

    draw_compare_for_sorting(n, samples_sorting)


if __name__ == "__main__":
    part_1()
