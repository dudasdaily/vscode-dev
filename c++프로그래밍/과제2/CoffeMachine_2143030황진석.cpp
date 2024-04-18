#include <iostream>
using namespace std;

class CoffeMachine{
    int coffe;
    int water;
    int sugar;

public:
    bool canCook = true;

    CoffeMachine() { coffe = 0; water = 0; sugar = 0; }
    CoffeMachine(int c, int w, int s)
    {
        coffe = c;
        water = w;
        sugar = s;

        while(coffe < 0 || coffe > 100)
        {
            cout << "0 <= coffe <= 100" << endl;
            cout << "Ŀ�� : ";
            cin  >> coffe;
        }

        while(water < 0 || water > 100)
        {
            cout << "0 <= water <= 100" << endl;
            cout << "�� : ";
            cin  >> water;
        }

        while(sugar < 0 || sugar > 100)
        {
            cout << "0 <= sugar <= 100" << endl;
            cout << "���� : ";
            cin  >> sugar;
        }
    }
    
    void show()
    {
        cout << "Ŀ�� �ӽ� ����, Ŀ��:" << coffe << " ��:" << water << " ����:" << sugar << endl;
    }

    void drinkEspresso()
    {
        if(coffe < 4 || water < 6)
        {
            cout << "���������Ҹ� ���� ��ᰡ �����մϴ�." << endl;
            canCook = false;
        }

        else
        {
            coffe -= 4;
            water -= 6;
            cout << "���������Ҹ� ��������ϴ�." << endl;        
        }
        
    }
    
    void drinkAmericano()
    {
        if(coffe < 2 || water < 7)
        {
            cout << "�Ƹ޸�ī�븦 ���� ��ᰡ �����մϴ�." << endl;
            canCook = false;
        }

        else
        {
            coffe -= 2;
            water -= 7;
            cout << "�Ƹ޸�ī�븦 ��������ϴ�." << endl;
        }
    }

    void drinkSugarCoffe()
    {
        if(coffe > 3 && water > 5 && sugar > 3)
        {
            coffe -= 3;
            water -= 5;
            sugar -= 3;
            cout << "���� Ŀ�Ǹ� ��������ϴ�." << endl;
        }
        
        else
        {
            cout << "���� Ŀ�Ǹ� ���� ��ᰡ �����մϴ�." << endl;
            canCook = false;
        }
    }

    void Refill()
    {
        if(coffe < 10)
        {
            int adjustment = 100 - coffe;
            cout << "Ŀ�Ǹ� " << adjustment << "��ŭ ä��ڽ��ϴ�." << endl;
            coffe += adjustment;
        }

        if(water < 10)
        {
            int adjustment = 100 - water;
            cout << "���� " << adjustment << "��ŭ ä��ڽ��ϴ�." << endl;
            water += adjustment;
        }

        if(sugar < 10)
        {
            int adjustment = 100 - sugar;
            cout << "������ " << adjustment << "��ŭ ä��ڽ��ϴ�." << endl;
            sugar += adjustment;
        }

        canCook = true;
    }

};

int main()
{
    CoffeMachine a(101, 15, 150);
    int userInput;

    do{
        cout << "[1. ����������, 2. �Ƹ޸�ī��, 3. ���� Ŀ��] �� ����(0�� �Է��ϸ� ����) > ";
        cin >> userInput;

        if(a.canCook == false)
            a.Refill();

        if(userInput == 1 && a.canCook == true)
        {
            a.drinkEspresso();
            a.show();
        }

        else if(userInput == 2 && a.canCook == true)
        {
            a.drinkAmericano();
            a.show();
        }

        else if(userInput == 3 && a.canCook == true)
        {
            a.drinkSugarCoffe();
            a.show();
        }
   
    }while(userInput != 0);


    return 0;
}