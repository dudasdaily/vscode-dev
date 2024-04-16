#include <iostream>
using namespace std;

class Circle {
	int radius;

public:
	int cnt = 0;

	Circle() { this->radius = 1; }
	
	Circle(int r)
	{
		this->radius = r;
	}

	void setradius(int r)
	{
		radius = r;
		if (radius >= 100)
			cnt++;
	}



};

int main()
{	
	Circle a[3];
	int r;
	int count = 0;
	
	for (int i = 0; i < 3; i++)
	{
		cout << "원 " << i + 1 << "의 반지름 : ";
		cin >> r;

		a[i].setradius(r);
		count += a[i].cnt;
	}

	cout << "면적이  100보다 큰 원은" << count << "개 입니다." << endl;



	//  실체.
	//  주소 ->

	return 0;
}