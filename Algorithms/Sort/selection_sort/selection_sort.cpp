#include "../sort.h"


void SelectionSort(int* array, uint length, bool isDescend)
{
    int selection;
    int temp;
    for (int i = 0; i != length; i++) {
        selection = i;
        for (int j = i + 1; j != length; j++) {
            if ((array[selection] > array[j]) ^ isDescend) {
                selection = j;
            }
        }
        temp = array[selection];
        array[selection] = array[i];
        array[i] = temp;
    }
}