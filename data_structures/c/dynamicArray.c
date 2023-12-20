/*

    Partial C implementation of the dynamic array in Recitation 2.
    Written for revising practical aspects of COMP2521.

    TODO:
    - Write tests?

*/

#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

typedef struct {
    int *arr;
    int  numI;
    int  numS;
} DA;

/*

    Helper functions for memory management

*/
DA *createDA() {
    DA *d = malloc(sizeof(DA));
    assert(d != NULL);

    d->arr = (int *)calloc(1, sizeof(int));
    assert(d->arr[0] == 0);
    /* TODO: Explanation of why *(arr->arr)[0] is...wrong*/

    d->numI = 0;
    d->numS = 1;

    return d;
}

void freeDA(DA *d) {
    free(d->arr);
    free(d);
}

void displayDA(DA *d) {
    printf("Occupied size: %d\n", d->numI);
    printf("[ ");
    for (int i = 0; i < d->numI; i++) {
        printf("%d", d->arr[i]);
        if (i < d->numI - 1) {
            printf(", ");
        }
    }
    printf(" ]\n");
    printf("Allocated size: %d\n", d->numS);
}


/*


*/
void _resize(DA *d) {
    ;
}

void _copy_forwards(DA *d) {
    ;
}

void _copy_backwards(DA *d) {
    ;
}

void insert_at(DA *d, int pos, int val) {
    ;
}

int delete_at(DA *d, int pos) {
    return -1;
}

/*
void insert_last(DA da)

*/

/*
    Simple test debugging code
*/

int main()  {
    /* Check creates empty array*/
    DA *d = createDA();
    displayDA(d);
    freeDA(d);

    /* Check init correctly */

    /* Check size doubling works*/

    /* Check size halving works */
    return 0;
}