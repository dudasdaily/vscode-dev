#include <iostream>
using namespace std;

int main()
{
    int a, b, cnt;

    cin >> cnt;

    int rst[cnt];

    for(int i = 0; i < cnt; i++)
    {
        cin >> a >> b;
        rst[i] = a + b;
    }

    for(int i = 1; i <= cnt; i++)
    {
        cout << "Case #" << i << ": " << rst[i - 1] << endl;
    }

    return 0;
}