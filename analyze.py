import random
import matplotlib
import matplotlib.pyplot
import time
LEFT_EDGE = -1000
RIGHT_EDGE = 1000


def generate_int_array(length:int):
    """Returns random integer array of 'length' elements"""
    return [random.randint(LEFT_EDGE, RIGHT_EDGE) for _ in range(length)]


def get_sorting_time(array:list[int]):
    """returns time needed to sort 'array'"""
    start_time = time.time_ns()
    array.sort()
    finish_time = time.time_ns()
    return finish_time - start_time


def get_summary_time(array:list[int]):
    """returns time needed to sum all elements of 'array'"""
    start_time = time.time_ns()
    sum(array)
    finish_time = time.time_ns()
    return finish_time - start_time


def get_square_time(array:list[int]):
    """returns time needed to square every element of 'array'"""
    start_time = time.time_ns()
    for i in range(len(array)):
        array[i] *= array[i]
    finish_time = time.time_ns()
    return finish_time - start_time


def part_1():
    n = [1, 2, 5, 7, 10, 15, 20, 30, 50, 70, 100, 150, 20000]

    samples_sorting = []
    for count in n:
        numbers = generate_int_array(count)
        execution_time = get_sorting_time(numbers)
        samples_sorting.append(execution_time)

    samples_summary = []
    for count in n:
        numbers = generate_int_array(count)
        execution_time = get_summary_time(numbers)
        samples_summary.append(execution_time)

    samples_square = []
    for count in n:
        numbers = generate_int_array(count)
        execution_time = get_square_time(numbers)
        samples_square.append(execution_time)

    matplotlib.pyplot.plot(n, samples_sorting)
    matplotlib.pyplot.plot(n, samples_summary)
    matplotlib.pyplot.plot(n, samples_square)

    matplotlib.pyplot.show()


if __name__ == "__main__":
    part_1()

#test
#test2
#test3
#артем я предлагаю пойти кушац
#погнали
#оп оп