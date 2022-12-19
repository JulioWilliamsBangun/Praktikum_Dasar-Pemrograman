#include <iostream>
using namespace std;
#define phi 3.14

int main() 
{
	int r;
	float luas,keliling;
	
	cout<<"Masukan jari-jari lingkaran : "; cin>>r;
	
	luas = phi*r*r;
	keliling = 2*phi*r;
	
	cout<<"Lingkungan dengan jari-jari :"<<r<<endl;cout<<"Mempunyai luas :"<<luas<<endl;
	cout<<"dan keliling : "<<keliling;
	
	return 0;
}
