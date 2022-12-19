#include <iostream>
using namespace std;

int main() 
{
	int jam,menit,detik,hasil;
	        cout<<"Masukan Jam : ";cin>>jam;
	        cout<<"Masukan Menit : ";cin>>menit;
	        cout<<"Masukan Detik :";cin>>detik;
	        
	hasil=(jam*3600)+(menit*60)+(detik);
	cout<<"Hasilnya : "<<hasil<<"detik";
	
	return 0;
}
