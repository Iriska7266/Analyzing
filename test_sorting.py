from algorithms import get_bubble_sort_time, get_sorting_time
from analyze import generate_int_array

def generating_list_to_sort(lenght, difficult):
    nums = []
    if difficult == 'sorted':
        for i in range(lenght):
            nums.append(i)

    elif difficult == 'unsorted':
        nums = generate_int_array(-1000, 1000, lenght)

    else:
        for i in range(lenght, -1, -1):
            nums.append(i)

    return nums

def main():
    lengths = [5, 50, 5000]
    difficulties = ['sorted', 'unsorted', 'rev sorted']

    for diffiluctie in difficulties:
        for length in lengths:
            list_numbers = generating_list_to_sort(length, diffiluctie)
            time1 = get_bubble_sort_time(list_numbers)
            time2 = get_sorting_time(list_numbers)
            print(f'Длинна {length}, положение искомого числа в списке {diffiluctie}, время поиска элемента по самописанному алгоритму {time1}, время поиска элемента по алгоритму "index": {time2}')

main()