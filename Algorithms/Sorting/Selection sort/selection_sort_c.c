#include <stdio.h>
#define MAXITEMS 10000

// function for printing an array
void print_array( int ar[],int size)
{
	for (int i = 0; i<size;i++)
	{
		printf("%d ",ar[i]);
	}
}

int main (void)
{
	int j=0,count = 0;
	int arr[MAXITEMS];
	int small,i,small_ind;
	
	//input numbers into array
	printf("Please, input numbers to sort. Use space as delimeter. Press Enter when finished.\n");
	do
	{
		scanf("%d",&arr[count++]);
	}
	while((getchar()!='\n') && (count<=10000));
	
	//selection sort algorithm
	small = arr[j];
	while (j<count)
	{		
		small = arr[j];
		for (i = j;i< count;i++)
		{
			if (arr[i]<small)
			{	
				small = arr[i];
				small_ind = i;
			}
		}

		if (arr[j]!=small)
		{
			int temp = arr[j];
			arr[j] = small;
			arr[small_ind] = temp;
		}
		++j;
	}
	
	print_array(arr, count);
}

