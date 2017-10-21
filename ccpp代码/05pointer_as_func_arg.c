#include <stdio.h>

void Increment_value(int a);
void Increment_reference(int* a);

int main(int argc, char const *argv[]) {
	int a; // local variable a (for main)
	a = 10;
	Increment_value(a); // a (from main) pass value to a (from Increment), they don't share address! call by value

	Increment_reference(&a);

	return 0;
}

void Increment_value(int a){
	a = a+1; // local variable a (for Increment)
}

void Increment_reference(int* a){
	*a = *a + 1;
}
// gcc -g -o test 05pointer_as_func_arg.c
// gdb test
