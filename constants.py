import numpy as np


"""Модуль предназначен для вычисления коэффициентов, необходимых для построения теоретических графиков
 разных сложностей алгоритмов
 Используется метод наименьших квадратов: c = sum(fact_time * th_func) / sum(th_func^2)"""


def calculate_c_for_n_log_n(n_values, actual_times):
    n_array = np.array(n_values)
    actual_array = np.array(actual_times)

    # Вычисляем n*log2(n) для каждого n
    n_log_n = n_array * np.log2(n_array)

    numerator = np.sum(actual_array * n_log_n)
    denominator = np.sum(n_log_n * n_log_n)
    c = numerator / denominator
    print(n_log_n,n_values)
    return c


def calculate_c_for_linear(n_values, actual_times):
    n_array = np.array(n_values)
    actual_array = np.array(actual_times)

    numerator = np.sum(actual_array * n_array)
    denominator = np.sum(n_array * n_array)
    c = numerator / denominator
    return c
