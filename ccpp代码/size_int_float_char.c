#include <stdio.h>
// #include <stdlib.h>

int main(int argc, char const *argv[]) {
	int a = 5;
	printf("int a = %d\n", a);
	printf("a_size = %ld\n", sizeof(a));


	float f = 5;
	printf("float f = %f\n", f);
	printf("f_size = %ld\n", sizeof(f));

	// char c = "5"; // 不能是双引号,双引号是string, arary, point?
	char c = '5';
	printf("char c = %c\n", c);
	printf("c_size = %ld\n", sizeof(c));
	return 0;
}

// gcc -g -o test size_int_float_char.c
// ./test
// gdb test
// start
// ctrl x a
// ctrl p | n
