#include <iostream>
using namespace std;

void sum_mean()
{
    int n = 0, cnt = 0, cumsum = 0;

    while(n < 100)
    {
        cin >> n;
        cnt++;
        cumsum += n;
    }
    
    cout << "합 : " << cumsum << " 평균 : " << float(cumsum / cnt) << endl;

}

int main()
{
    sum_mean();   

    return 0;
}