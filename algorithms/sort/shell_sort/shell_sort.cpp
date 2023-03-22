#include "../sort.h"

#include <iostream>

void ShellSort(int* array, uint length, bool isDescend)
{
    int i, j, gap, key;
    for (gap = length / 2; gap > 0; gap /= 2) {
        for (i = gap; i < length; i++) {
            key = array[i];
            for (j = i - gap; j > -1 && ((array[j] > key) ^ isDescend); j -= gap)
                array[j + gap] = array[j];
            array[j + gap] = key;
        }
    }
}