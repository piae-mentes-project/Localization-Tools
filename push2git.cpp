#include <iostream>
#include <cstring>

using namespace std;

int main(){
	string msg;
	cout<<"Please add Git to PATH!";
	cout<<"Commit Massage:";
	cin>>msg;
	string command="git commit -m";
	command+=msg;
	system("chcp 65001");
	system("git add .");
	system(command.data());
	system("git push origin main");
	return 0;
}