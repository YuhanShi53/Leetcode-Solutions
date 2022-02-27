#include <iostream>

#include "sort/sort.h"

int main()
{
    const uint length = 5;
    int array[length] = {8, 2, 4, 0, 1};
    BubbleSort(array, length, false);
    for (int i = 0; i < length; i++) {
        std::cout << array[i] << std::endl;
    }
}
