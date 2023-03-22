def insertion_sort(x, is_descend=False):
    for i in range(len(x)):
        key = x[i]
        j = i - 1
        while (j >= 0) & ((x[j] > key) ^ is_descend):
            x[j+1] = x[j]
            j -= 1
        x[j+1] = key


if __name__ == "__main__":
    x = [9, 1, 2, 4, 5, 7, 3, 7, 9]
    insertion_sort(x, False)
    print(x)
