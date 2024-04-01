#include <iostream>
using namespace std;

void oddsum(int n)
{
    int result = 0;

    for(int i = 1; i <= n; i++)
        if(i % 2 != 0)
            result += i;
 
    cout << result << endl;            
}

void evensum(int n)
{
    int result = 0;

    for(int i = 1; i <= n; i++)
        if(i % 2 == 0)
            result += i;
 
    cout << result << endl;            
}

int main()
{
    int n;
    cin >> n;
    while(n > 50)
    {
        cout << "submit under 50" << endl;
        cin >> n;
    }

    oddsum(n);
    evensum(n);

    return 0;
}