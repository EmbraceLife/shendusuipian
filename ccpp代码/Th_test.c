#include <TH/TH.h>

int main()
{
    THFile *x_file = THDiskFile_new("x", "r", 0);
    THFile *y_file = THDiskFile_new("y", "r", 0);

    THFloatTensor *x = THFloatTensor_newWithSize1d(10);
    THFloatTensor *y = THFloatTensor_newWithSize1d(10);

    THFile_readFloat(x_file, x->storage);
    THFile_readFloat(y_file, y->storage);

    double result = THFloatTensor_dot(x, y) + THFloatTensor_sumall(x);

    printf("%f\n", result);

    THFloatTensor_free(x);
    THFloatTensor_free(y);
    THFile_free(x_file);
    THFile_free(y_file);
    return 0;
}
