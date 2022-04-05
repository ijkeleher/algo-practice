"""
This is a collection of sorting algos
"""
import sys
import random
import time


def py_sort(items: list[int]) -> list:
    """
    This func returns a sorted list using default python sorting algo
    """
    return sorted(items)


def insertion_sort(items: list[int]) -> list:
    """
    Returns a sorted list using insertion sort
    """
    # Loop from the second element of the items until
    # the last element
    for i in range(1, len(items)):
        # This is the element we want to position in its
        # correct place
        key_item = items[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the items) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and items[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            items[j + 1] = items[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        items[j + 1] = key_item

    return items


if __name__ == "__main__":

    # Generate 6 random numbers between 10 and 30
    u_lst = random.sample(range(1, 99), 50)

    start_time = time.time()

    # to run program use `python3 sort.py [function_name]``
    # e.g. `python3 sort.py insertion_sort` to use insertion_sort

    print(f'\nunsorted: \n{u_lst} \n\nsorted: \n{globals()[sys.argv[1]](u_lst)}')

    # print out the runtime non-inclusive of list gen
    print(f"\n --- Total Time: {time.time() - start_time} seconds ---")
