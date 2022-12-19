#include <iostream>
#include <math.h>
using namespace std;
int main() 
{
	int alas,tinggi,sisi_miring;
	
	cout<<"Peogram penghitung sisi miring segitiga"<<endl;
	cout<<"Masukan ukuran alas : "; cin>>alas;cout<<endl;
	cout<<"Masukan ukuran tinggi :"; cin>>tinggi;cout<<endl;
	
	sisi_miring = sqrt((alas*alas)+(tinggi*tinggi));
	
	cout<<"Jadi panjang sisi miring segitiga tersebut adalah : "<<sisi_miring;
	return 0;
}
