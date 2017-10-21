#include <stdio.h>

// void Double(int A[], int size);
void Double(int* A, int size);

int main(int argc, char const *argv[]) {
	int A[] = {1,2,3,4,5};
	int size = sizeof(A)/sizeof(A[0]);
	int i;
	Double(&A, size);
	for (i=0; i<size; i++)
	{
		printf("%d", A[i]);
	}
	return 0;
}

void Double(int* A, int size)
{
	int i, sum = 0;
	for (i = 0; i < size; i++)
	{
		A[i] = A[i] * 2;
	}
}
// gcc -g -o test 07array_as_func_args.c
// gdb test
