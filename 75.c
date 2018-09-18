#include<string.h>
int main() 
{
	char s[30];
	int n,i;
	printf("");
	scanf("%s",s);
	n=strlen(s);
	if(n%2==0)
	{
		s[n/2]='*';
		s[(n/2)-1]='*';
	}
	else
	{
		s[n/2]='*';
	}
	printf(s);
	return 0;
}
