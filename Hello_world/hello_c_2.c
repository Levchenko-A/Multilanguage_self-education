#include <stdio.h>

int main(void)
{
	char message[]= "Hello,C! - 2";
	int len_message = sizeof(message)/sizeof(message[0]);
	for (int i=0; i<len_message;i++)
	{
		printf("%c",message[i]);
	}
	printf("\n");
	
}
