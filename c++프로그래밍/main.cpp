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
		cout << "�� " << i + 1 << "�� ������ : ";
		cin >> r;

		a[i].setradius(r);
		count += a[i].cnt;
	}

	cout << "������  100���� ū ����" << count << "�� �Դϴ�." << endl;



	//  ��ü.
	//  �ּ� ->

	return 0;
}