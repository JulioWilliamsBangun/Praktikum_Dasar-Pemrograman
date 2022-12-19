#include <iostream>
using namespace std;

int main() 
{
	int total_detik,jam,menit,sisa,detik;
	
	cout<<"Masukan detik yang akan diubah :"; cin>>total_detik;
	
	jam = total_detik/3600;
	sisa = total_detik%3600;
	menit = sisa/60;
	detik = sisa%60;
	
	cout<<"Hasil konversi detik"<<endl;
	cout<<total_detik;cout<<"";cout<<"detik adalah "<<endl;
	
	cout<<jam; cout<<"_jam"<<endl;
	cout<<menit; cout<<"_menit"<<endl;
	cout<<detik; cout<<"_detik"<<endl;
	
	return 0;
	
}
	
