#include <stdio.h>

int main(void)
{
	int count = 0;
	int arr[10000];
	int temp;
	
	//input numbers into array
	printf("Please, input numbers to sort. Use space as delimeter. Press Enter when finished.\n");
	do
	{
		scanf("%d",&arr[count++]);
	}
	while((getchar()!='\n') && (count<=10000));
	
	//bubble sort algorithm
	for (int i = 0; i<(count-1);i++)
	{
		for (int j = i; j<count;j++)
		{
			if (arr[j]<arr[i])
			{
				temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
	}
	
	//output of the sorted array
	printf("This is your sorted array:\n");
	for (int i = 0; i<count;i++)
	{
		printf("%d ",arr[i]);
	}
	
}
