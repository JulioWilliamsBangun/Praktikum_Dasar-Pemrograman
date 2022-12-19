#include <iostream>
using namespace std;
int main() 
{
	    int kode_hari;
	    cout<<"Menentukan hari\n";
	    cout<<"1 = SENIN 3 =RABU 5 =JUMAT 7 =MINGGU\n";
	    cout<<"2 = SELASA 4 =KAMIS 6 =SABTU";
	    cout<<"\nMasukan kode hari (1..7): ";
	    cin>>kode_hari;
	    switch(kode_hari)
	    {
		    case 1:
		    	   cout<<"Hari SENIN"<<endl;
		    	   break;
		    case 2:
		    	   cout<<"Hari SELASA"<<endl;
		    	   break;
			case 3:
		    	   cout<<"Hari RABU"<<endl;
		    	   break;
			case 4:
		    	   cout<<"Hari KAMIS"<<endl;
		    	   break;
			case 5:
		    	   cout<<"Hari JUMAT"<<endl;
		    	   break;
			case 6:
		    	   cout<<"Hari SABTU"<<endl;
		    	   break;
			case 7:
		    	   cout<<"Hari MINGGU"<<endl;
		    	   break;
			default:cout<<"Kode yang anda masukan salah"<<endl;
	}
}
