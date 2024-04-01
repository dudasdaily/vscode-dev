#include <iostream>
using namespace std;


void circle_area(float r)
{
    cout << "원넓이 : " << r * 3.141592 << endl;
}
int main()
{
    float r = 0;

    cout << "반지름 입력 : ";
    cin >> r;

    circle_area(r);

    
    return 0;
}