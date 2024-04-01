#include <iostream>
using namespace std;

void gugudan(int a, int b)
{
    for( ; a <= b; a++)
    {
        cout << endl;
        
        for(int i = 1; i <= 9; i++)
        {
            cout << a << "*" << i << " = " << a * i << endl; 
        }

        cout << endl;
    }

}

int main()
{
    int a, b;

    do{
        cin >> a >> b;
    }while(a >= b);
    
    gugudan(a, b);



    return 0;
}