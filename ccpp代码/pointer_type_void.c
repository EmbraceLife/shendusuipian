#include <stdio.h>

int main(int argc, char const *argv[]) {
	int a = 1025;
	int* p;
	p = &a;
	/* p sizeof(int), sizeof(p) or sizeof(*p)
	** p p, *p
	** p p+1, *(p+1)
	**
	*/
	char* p0;
	p0 = (char*)p; // typecasting
	/* p sizeof(char), sizeof(p), sizeof(p0)
	** p p0, *p0, p0+1, *(p0+1)
	*/

	void* p1;
	p1 = p;
	return 0;
}

// gcc -g -o test pointer_type_void.c
// gdb test
// ctrl + x + a
