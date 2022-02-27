#include "../sort.h"

void BubbleSort(int* array, uint length, bool isDescend = false)
{
    bool isSorted;
    for (uint i = 0; i < length; i++){
        isSorted = true;
        int temp;
        for (uint j = 1; j < length - i; j++){
            if ((array[j-1] > array[j]) ^ isDescend){
                temp = array[j-1];
                array[j-1] = array[j];
                array[j] = temp;
                isSorted = false;
            }
        }
        if (isSorted)
            break;
    }
}
