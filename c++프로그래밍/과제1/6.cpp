#include <iostream>
using namespace std;

int facto(int n)
{
    int a;

    if(n > 0)
    {
        a = n * facto(n-1);
    }

    else if(n == 0)
        return 1;

    return a;
}

int main()
{
    int n;

    cout << "n을 입력하시오 : ";
    cin >> n;

    cout << n << "! = " << facto(n) << endl;

    return 0;
}