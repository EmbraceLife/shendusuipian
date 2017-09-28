#include <stdio.h>

int printSomething()
{
	printf("I will not be executed");
	return 0;
}

int main()
{
	printf("I'm a great guy, \n ");
	printSomething();
	return 0;
}
