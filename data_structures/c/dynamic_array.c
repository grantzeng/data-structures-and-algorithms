/*
    Partial C implementation of the dynamic array in Recitation 2
*/

#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

typedef struct DA {
    int *arr;
    size_t  numI;
    size_t  numS;
}

/*
    Helper functions for memory management

*/
DA *createDA() {

    DA *d = malloc(sizeof(struct DA));
    assert(d != NULL);

    d->arr = (int *)calloc(sizeof(int));
    assert(arr->arr[0] == 0); /* *(arr->arr)[0] is...wrong*/

    d->numI = 0;
    d->numS = 1;

    return arr;
}

void freeDA(DA d) {
    ;
}


/*


*/
void insert_at(DA arr, int pos, int val) {
    ;
}

int delete_at(DA arr, int pos) {
    ;
}

/*
void insert_last(DA da)

*/

/*
    Simple test debugging code
*/

int main()  {

    /* Check init correctly */

    /* Check size doubling works*/

    /* Check size halving works */
}