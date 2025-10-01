from algorithms import get_bubble_sort_time, get_sorting_time
from algorithms import RIGHT_EDGE, LEFT_EDGE, generate_int_array


def generating_list_to_sort(length, difficulty):
    nums = []
    if difficulty == 'sorted':
        for i in range(length):
            nums.append(i)

    elif difficulty == 'unsorted':
        nums = generate_int_array(LEFT_EDGE, RIGHT_EDGE, length)

    elif difficulty == 'rev sorted':
        for i in range(length, -1, -1):
            nums.append(i)

    return nums

def main():
    lengths = [5, 50, 5000]
    difficulties = ['sorted', 'unsorted', 'rev sorted']

    for difficulty in difficulties:
        for length in lengths:
            numbers_list = generating_list_to_sort(length, difficulty)
            time1 = get_bubble_sort_time(numbers_list)
            time2 = get_sorting_time(numbers_list)
            print(f'Длина {length}, набор данных {difficulty}, время сортировки по собственному алгоритму "bubble sort" {time1}, время сортировки по алгоритму "sort": {time2}')
