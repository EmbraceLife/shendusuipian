#include <stdio.h>

int main(int argc, char const *argv[]) {
	int A[] = {2,4,5,8,1};
	int* p;
	p = &A[0];
	// *p, &A[1], p+1, A[1], *(p+1)

	p = A; // => p = &A[0], A is a pointer to A[0]
	// A, *A, A+1, *(A+1)

	// p++, A++
	// A = A+1;
	return 0;
}

// gcc -g -o test 06pointer_arrays.c
// gdb test
