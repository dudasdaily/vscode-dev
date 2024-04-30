#include <iostream>
using namespace std;

class Circle {
public:
	static int a;
};
// os -> static int a -> main -> Circle 객체
// 따라서 static은 this랑 같이 못씀

int main()
{
	// static은 제일 먼저 생성되서 제일 나중에 삭제됨
	static int a; // (스택) os -> static int a -> main -> ....

	


	return 0;
}

// 문자열 복사, 문자열 비교, 문자열 길이, 부분 문자열, 특정 문자열 찾기

// string.substr(시작위치, 개수)
// string.substr(시작위치) : 시작위치부터 끝까지 끊어버림
// string.find('string', 시작위치)
// string.find(str, 시작위치) 
// string.replace(시작위치, 길이, 변경문자열)
// cin.ignore() : 입력버퍼 비우기
