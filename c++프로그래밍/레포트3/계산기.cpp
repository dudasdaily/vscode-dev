#include <iostream>
#include <string>
using namespace std;

class Node {
	string item;
	Node* next;

public:
	Node()
	{
		item = "Dummy";
		next = 0;
	}

	Node(string item, Node* next)
	{
		this->item = item;
		this->next = next;
	}

	void setItem(string item) { this->item = item; }
	void setNext(Node* next) { this->next = next; }
	string getItem() { return item; }
	Node* getNext() { return next; }
};

class Stack {
	int numItems;
	Node* head = new Node();

public:
	Stack() { numItems = 0; }

	Node* getNode(int index)
	{
		if (numItems == 0)
			return head;

		else if (index >= numItems) { cout << "Failed getNode(), Out of Bounds" << endl; }

		else
		{
			Node* curr = head;

			for (int i = 0; i < index + 1; i++)
			{
				curr = curr->getNext();
			}

			return curr;
		}
	}

	void push(string item)
	{
		Node* curr = getNode(numItems - 1);

		Node* newNode = new Node(item, 0);
		curr->setNext(newNode);

		numItems += 1;
	}

	void push(char item)
	{
		string a;
		a += item;

		Node* curr = getNode(numItems - 1);

		Node* newNode = new Node(a, 0);
		curr->setNext(newNode);

		numItems += 1;
	}

	string pop()
	{
		if (numItems <= 0)
			cout << "There is no Item in Stack" << endl;

		else
		{
			Node* curr = getNode(numItems - 1);
			string rtn = curr->getItem();

			delete curr;
			numItems -= 1;

			return rtn;
		}
	}

	void printStack()
	{
		if (numItems <= 0)
			cout << "There is no Item in Stack" << endl;

		else
		{
			Node* curr = head;

			for (int i = 0; i < numItems; i++)
			{
				curr = curr->getNext();
				cout << curr->getItem() << " ";
			}

			cout << endl;
		}
	}

	string top()
	{
		if (numItems <= 0)
			cout << "There is no Item in Stack" << endl;

		else
		{
			Node* curr = getNode(numItems - 1);
			string rtn = curr->getItem();

			return rtn;
		}
	}

	bool isempty()
	{
		if (numItems == 0)
			return true;

		else
			return false;
	}

	int getNumItems() { return numItems; }
};

bool isdigit(char c)
{
	if ('0' <= c && c <= '9')
	{
		return true;
	}

	else
		return false;
}

int priority(char c)
{
	if (c == '+' || c == '-')
		return 1;

	else if (c == '*' || c == '/')
		return 2;
}

void eval(Stack& ans, char oper)
{
	if (ans.getNumItems() >= 2)
	{
		int a = stoi(ans.pop());
		int b = stoi(ans.pop());
		
		if (oper == '+')
			ans.push(to_string(b + a));

		else if (oper == '-')
			ans.push(to_string(b - a));

		else if (oper == '*')
			ans.push(to_string(b * a));

		else if (oper == '/')
			ans.push(to_string(b / a));
	}

	else
		cout << "Error" << endl;
}

int mid2post(string s)
{
	Stack oper;
	Stack ans;
	bool isbeforedigit = false;
	
	char c;

	for (int i = 0; i < s.length(); i++)
	{
		c = s[i]; // 입력받은 문자열을 하나씩 체크

		if ('0' <= c && c <= '9')
		{
			if (isbeforedigit == true)
			{
				int tmp = stoi(ans.pop());
				tmp = (tmp * 10) + (c - '0');

				ans.push(to_string(tmp));
			}

			else
				ans.push(c);

			isbeforedigit = true;
		}

		else if (c == '+' || c == '-' || c == '*' || c == '/')
		{
			isbeforedigit = false;

			if (oper.isempty())
			{
				oper.push(c);
			}

			else if (priority(c) > priority(oper.top()[0]))
			{
				oper.push(c);
			}

			else if (priority(c) <= oper.top()[0])
			{
				while (!oper.isempty() && priority(c) <= priority(oper.top()[0]))
				{
					eval(ans, oper.pop()[0]);
				}

				oper.push(c);
			}
		}
	}

	while (!oper.isempty())
	{
		eval(ans, oper.pop()[0]);
	}

	return stoi(ans.pop());
}

int main()
{
	string s;
	getline(cin, s, '\n');

	cout << mid2post(s) << endl;

	return 0;
}
