#include <stdio.h>
// #include <stdlib.h>

int main(int argc, char const *argv[]) {
	int a; // print a, &a, sizeof(a)

	int* p; // print p, *p
	p = &a; // print p, *p
	a = 5; // print p, *p
	*p = 8;

	return 0;
}

// gcc -g -o test pointer_address_value.c
// ./test
// gdb test
// start
// ctrl x a
// ctrl p | n
