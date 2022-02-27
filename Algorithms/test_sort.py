from sort import bubble_sort, insertion_sort


if __name__ == "__main__":
    array = [9, 4, 3, 0, 1]
    bubble_sort(array, is_descend=True)
    print(array)

    bubble_sort(array, is_descend=False)
    print(array)
