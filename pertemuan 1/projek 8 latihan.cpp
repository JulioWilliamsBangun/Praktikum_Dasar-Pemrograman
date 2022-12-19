#include <stdio.h>
#include <conio.h>

int main() 
{
	int m,n;
	
	printf("Menampilkan deret bilangan ganjil ke n : ");
	scanf("%d",&n);
	
	for (m = 1;m<n;m++)
	{
		if (m%2 !=0)
		printf("%d",m);
		
	}
	getch();
}
