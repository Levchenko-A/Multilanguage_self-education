import random


def create_array(size, minimum, maximum):
    """
    creating an array of a given size filled with random numbers.
    size - int, size of an array;
    minimum - minimum value of the range for random number generation;
    maximum - maximum value of the range for random number generation;
    arr - list, return value, array.
    """

    arr = []
    for i in range(size):
        arr.append(random.randint(minimum, maximum))
    return arr


def binary_search(target_value, arr):
    """
    algo of a binary search.
    target_value - int, value to find in an array
                    (we want to find an index of this value in an array);
    arr - list, array to search in;
    guess - int,return value, index of a guess-value.
    """

    lower_limit = 0
    higher_limit = len(arr) - 1
    while lower_limit <= higher_limit:
        guess = int((lower_limit + higher_limit) / 2)
        if arr[guess] == target_value:
            return guess
        if arr[guess] < target_value:
            lower_limit = guess + 1
        else:
            higher_limit = guess - 1
    return None


TARGET = 30
RANDOM_RANGE_MIN = 0
RANDOM_RANGE_MAX = 1000
ARRAY_LEN = 1000

new_array = create_array(ARRAY_LEN, RANDOM_RANGE_MIN, RANDOM_RANGE_MAX)
new_array = sorted(new_array)
index_of_guess = binary_search(TARGET, new_array)
print(index_of_guess)
