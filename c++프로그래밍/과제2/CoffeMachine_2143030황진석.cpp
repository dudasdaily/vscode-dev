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
            cout << "커피 : ";
            cin  >> coffe;
        }

        while(water < 0 || water > 100)
        {
            cout << "0 <= water <= 100" << endl;
            cout << "물 : ";
            cin  >> water;
        }

        while(sugar < 0 || sugar > 100)
        {
            cout << "0 <= sugar <= 100" << endl;
            cout << "설탕 : ";
            cin  >> sugar;
        }
    }
    
    void show()
    {
        cout << "커피 머신 상태, 커피:" << coffe << " 물:" << water << " 설탕:" << sugar << endl;
    }

    void drinkEspresso()
    {
        if(coffe < 4 || water < 6)
        {
            cout << "에스프레소를 만들 재료가 부족합니다." << endl;
            canCook = false;
        }

        else
        {
            coffe -= 4;
            water -= 6;
            cout << "에스프레소를 만들었습니다." << endl;        
        }
        
    }
    
    void drinkAmericano()
    {
        if(coffe < 2 || water < 7)
        {
            cout << "아메리카노를 만들 재료가 부족합니다." << endl;
            canCook = false;
        }

        else
        {
            coffe -= 2;
            water -= 7;
            cout << "아메리카노를 만들었습니다." << endl;
        }
    }

    void drinkSugarCoffe()
    {
        if(coffe > 3 && water > 5 && sugar > 3)
        {
            coffe -= 3;
            water -= 5;
            sugar -= 3;
            cout << "설탕 커피를 만들었습니다." << endl;
        }
        
        else
        {
            cout << "설탕 커피를 만들 재료가 부족합니다." << endl;
            canCook = false;
        }
    }

    void Refill()
    {
        if(coffe < 10)
        {
            int adjustment = 100 - coffe;
            cout << "커피를 " << adjustment << "만큼 채우겠습니다." << endl;
            coffe += adjustment;
        }

        if(water < 10)
        {
            int adjustment = 100 - water;
            cout << "물을 " << adjustment << "만큼 채우겠습니다." << endl;
            water += adjustment;
        }

        if(sugar < 10)
        {
            int adjustment = 100 - sugar;
            cout << "설탕을 " << adjustment << "만큼 채우겠습니다." << endl;
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
        cout << "[1. 에스프레소, 2. 아메리카노, 3. 설탕 커피] 중 선택(0을 입력하면 종료) > ";
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