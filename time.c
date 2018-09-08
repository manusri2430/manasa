#include<stdio.h>
int main()
{
	int min,hr,m;
	printf("\n");
	scanf("%d",&min);
	hr=min/60;
	min=min%60;
	printf("\n %d %d",hr,min);
	return 0;
	
}
