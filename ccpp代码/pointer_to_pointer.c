#include <stdio.h>

int main(int argc, char const *argv[]) {
	int x = 5;
	int* p;
	p = &x;
	*p = 6;
	int** q;
	q = &p; // print q, *q, **q
	int*** r = &q;
	***r = 10;
	**q = *p + 2;

	return 0;
}

// gcc -g -o test pointer_to_pointer.c
// gdb test
