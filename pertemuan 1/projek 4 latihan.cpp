#include <iostream>
#define phi 3.14 
using namespace std;
int main() 
{
	int r;
	float luas_lingkaran;
	
	cout<<"Masukan jari-jari lingkaran :"; cin>>r;
	
	luas_lingkaran = phi*r*r;
	
	cout<<"Luas Lingkaran : "<<luas_lingkaran;
	
	return 0;
}
