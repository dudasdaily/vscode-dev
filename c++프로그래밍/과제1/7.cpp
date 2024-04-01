#include <iostream>
using namespace std;

 
void swapArray(int *p, int *q, int size) // p, q�� �迭�� ����Ű��, size�� �迭�� ũ��
{
    int temp[size];

    for(int i = 0; i < size; i++)
    {
        temp[i] = p[i];
        p[i] = q[i];
        q[i] = temp[i];
    }

    cout << "������ �Ϸ��߽��ϴ�." << endl;

}    
void printArray(int *p, int size) // p�� �迭�� ����Ű��, size�� �迭�� ũ��
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