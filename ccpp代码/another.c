#include <stdio.h>

int main(){
	int a = 10;
	int* p;
	p = &a; // logical

	int* p1 = &a; // kind of ok

	int* p2;
	// *p2 = a; // not working, but no address value
	// *p2 = &a; // not working, as no logic

	// print p, p + 1
	return 0;
}
