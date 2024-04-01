#include <iostream>
using namespace std;

int is_zero(int* arr, int arr_size) // 인덱스를 리턴할거임.
{
    for(int i = 0; i < arr_size; i++)
    {
        cin >> arr[i];

        if(arr[i] == 0)
        {
            cout << "입력 완료" << endl;
            return i;
        }
    }

    return 99;
}

int main()
{
    int arr[100];
    int index = is_zero(arr, 100);

    cout << "역순으로 출력" << endl;
    for( ; index > 0; index--)
        cout << arr[index] << endl;


    return 0;
}