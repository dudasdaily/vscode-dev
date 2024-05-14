#include <iostream>
#include <string>d
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

		else if (index >= numItems)
			cout << "Failed getNode(), Out of Bounds" << endl;

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
};



int main()
{

	return 0;
}
