#include <stdio.h>

int fact(int x);
int res;

int main(void)
{
	int number,result;
	
	printf("Please, enter a number to find it`s factorial: \n");
	scanf("%d",&number);
	printf("You have entered a number: %d\n", number);
	result = fact(number);
	printf("Factorial of %d is %d.\n",number,result);
	return 0;
}

/* A recursive function to find factorial of a number*/
int fact(int x)
{	
	if (x != 1)
	{
		res = x*fact(x-1);
	}
	else
	{
		res = 1;
	}
	return res;
}