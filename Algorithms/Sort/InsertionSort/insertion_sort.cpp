#include <iostream>

void insertion_sort(int* array, unsigned int n, bool isDescend = false)
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

int main()
{
    const unsigned int n = 7;
    int array[n] = {9, 2, 3, 1, 6, 4, 0};
    insertion_sort(array, n, true);
    for (auto x : array) {
        std::cout << x << std::endl;
    }
}