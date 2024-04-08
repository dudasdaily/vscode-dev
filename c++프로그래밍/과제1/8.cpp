#include <iostream>
using namespace std;

int maximum(int* arr, int size)
{
    int max = arr[0];

    for(int i = 0; i < size; i++)
    {
        if(max <= arr[i])
            max = arr[i];   
    }

    return max;
}

int minimum(int* arr, int size)
{
    int min = arr[0];

    for(int i = 0; i < size; i++)
    {
        if(min >= arr[i])
            min = arr[i];
    }

    return min; 
}

int main()
{
    int array[10] = { 9, 5, 11, 4, 1, 3, 7, 12, 2, 8 };
    int size = sizeof(array) / sizeof(int);

    cout << "max : " << maximum(array, size) << " min : " << minimum(array, size) << endl;

    return 0;
}