#include <stdio.h>
#include <stdlib.h>

void passByValue(int i); // must have, otherwise won't work
void passByAddress(int *i);
/*
 *
 */
int main(int argc, char** argv) {

    int tuna = 20;
    passByValue(tuna); // tuna's memory is 20, this func won't replace memory
    printf("passByValue return %d \n", tuna);

    passByAddress(&tuna); // tuna's memory is overwritten here to 64 from 20
    printf("passByAddress return %d", tuna);

    return (EXIT_SUCCESS);
}

void passByAddress(int *i){
    *i = 64;
    return;
}

void passByValue(int i){
    i = 99;
    return;
}

// gcc -g -o value_address main.c
// gdb value_address
