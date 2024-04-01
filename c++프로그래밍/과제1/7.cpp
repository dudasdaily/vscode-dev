#include <iostream>
using namespace std;

 
void swapArray(int *p, int *q, int size) // p, q는 배열을 가리키고, size는 배열의 크기
{
    int temp[size];

    for(int i = 0; i < size; i++)
    {
        temp[i] = p[i];
        p[i] = q[i];
        q[i] = temp[i];
    }

    cout << "스왑을 완료했습니다." << endl;

}    
void printArray(int *p, int size) // p는 배열을 가리키고, size는 배열의 크기
{
    for(int i = 0; i < size; i++)
        cout << p[i] << ' ';
    
    cout << endl;
}

int main()
{
    int a[] = {1,2,3,4,5};
    int b[] = {9,8,7,6,5};

    cout << " a = "; printArray(a, 5);
    cout << " b = "; printArray(b, 5);

    swapArray(a, b, 5);
    cout << " a = "; printArray(a, 5);
    cout << " b = "; printArray(b, 5);

}