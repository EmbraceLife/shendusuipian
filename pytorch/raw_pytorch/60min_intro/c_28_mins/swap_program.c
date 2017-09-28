#include <stdio.h>

//Assignment Operator

///////////   ///////////
//   10    //    //  10     //
//////////    //////////
// i               j

//score - integer
int main()
{
	int i=5;
	int j=10;
	int k;

	k = i;//k=5,i=5,j=10
	i=j;//k=5,i=10,j=10
	j=k;//k=5,i=10,j=5

	printf("i:%d j:%d",
			i,j);

	return 0;
}
