#include <iostream>

#include "../sort.h"

void InsertionSort(int* array, uint n, bool isDescend = false)
{
    int key;
    int j;
    for (int i = 1; i < n; i++){
        key = array[i];
        j = i - 1;
        while(j >= 0 && (key < array[j]) ^ isDescend){
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = key;
    }
}
