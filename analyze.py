import matplotlib
import matplotlib.pyplot
import math
from constants import *
from algorithms import *
import test_find
import test_sorting


def draw_plot_with_attributes():
    matplotlib.pyplot.xlabel("Count of numbers")
    matplotlib.pyplot.ylabel("Time, ns")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()


def draw_execution_time(n: list[int], samples_sorting: list[int|float],
                                      samples_summary: list[int|float],
                                      samples_square: list[int|float],):
    matplotlib.pyplot.plot(n, samples_sorting, label="Sorting")
    matplotlib.pyplot.plot(n, samples_summary, label="Summary")
    matplotlib.pyplot.plot(n, samples_square, label="Square")

    matplotlib.pyplot.title("Execution time")
    draw_plot_with_attributes()


def draw_compare_for_sorting(n, sort_time: list[int|float], c: int|float):
    """Common sort function has O(n*log(n)) difficulty"""
    y = [i * math.log2(i) * c for i in n]
    matplotlib.pyplot.plot(n, sort_time, label="Fact time")
    matplotlib.pyplot.plot(n, y, label="Expecting time")

    matplotlib.pyplot.title("1. Sorting algorithm")
    draw_plot_with_attributes()


def draw_compare_for_summary(n: list[int], sum_time: list[int|float], c: int|float):
    """Common sum function has O(n) difficulty"""
    y = [i * c for i in n]
    matplotlib.pyplot.plot(n, sum_time, label="Fact time")
    matplotlib.pyplot.plot(n, y, label="Expecting time")

    matplotlib.pyplot.title("2. Summary algorithm")
    draw_plot_with_attributes()


def draw_compare_for_square(n: list[int], sum_time: list[int|float], c: int|float):
    """Our square function has O(n) difficulty"""
    y = [i * c for i in n]
    matplotlib.pyplot.plot(n, sum_time, label="Fact time")
    matplotlib.pyplot.plot(n, y, label="Expecting time")

    matplotlib.pyplot.title("3. Square algorithm")
    draw_plot_with_attributes()


def part_1():
    # n = [10000, 11000, 12000, 13000, 14000, 15000]
    n = [1, 2, 5, 7, 10, 15, 20, 30, 50, 70, 100, 150, 200]

    samples_sorting = []
    samples_summary = []
    samples_square = []

    # Getting time of every algorithm execution with different counts of numbers
    for count in n:
        numbers = generate_int_array(LEFT_EDGE,RIGHT_EDGE,count)

        time_sort = get_sorting_time(numbers)
        time_sum = get_summary_time(numbers)
        time_square = get_square_time(numbers)

        samples_sorting.append(time_sort)
        samples_summary.append(time_sum)
        samples_square.append(time_square)

    draw_execution_time(n, samples_sorting, samples_summary, samples_square)

    c = calculate_c_for_n_log_n(n, samples_sorting)
    draw_compare_for_sorting(n, samples_sorting, c)

    c = calculate_c_for_linear(n, samples_summary)
    draw_compare_for_summary(n, samples_summary, c)

    c = calculate_c_for_linear(n, samples_square)
    draw_compare_for_square(n, samples_square, c)


def part_2():
    print("First algorithm 'sorting':")
    test_sorting.main()
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Second algorithm 'find index':")
    test_find.main()


if __name__ == "__main__":
    part_1()
    part_2()
