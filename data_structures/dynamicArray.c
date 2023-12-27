/*

    Partial C implementation of the dynamic array in Recitation 2.
    Written for revising practical aspects of COMP2521.

    TODO:
    - Think about test cases/write some shell script to run it against the Python implementations

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

    /* TODO: Add ability to init with a static array */

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

    ARRAY RESIZING POLICY

    > "Cookies are a _sometimes_ food, according to modern Cookie Monster" - Lec 2

    Idea:
    - Make it s.t. if we do n inserts, it should cost us at most O(n) time, i.e.
      amortized O(1) versus the original policy with the dumb array where we do +1
      each time (so 1 insert costs O(n) time because of all the copying, which is
      the expensive operation we want to make rare)

    - If we're not really _using_ the allocated memory e.g. popped a lot of elements,
      we want to _deallocate_ extra space. But we also want to do this in amortized O(1).

    Resizing policy:
    - if numI same as size, trigger table doubling.
    - if numI < half of size, trigger table halving.

    Proof results in amortized O(1) insert_last:
    - Suppose we insert_last n items 1, 2, 3, ..., n

    - With table doubling policy, we pay O(n) resize cost (allocation and copying)
      every 1, 2, 4, ..., k=(nearest power of 2 less than n) which is just a geometric
      series \sum_{log k}{i=0} 2^i = 2^{k+1} - 1

    - but this is just O(.) of the highest term which is roughly 2^{\log(n)} so total cost is O(n)

    - voila, O(1) amortized across all n inserts

    TODO: Figure out how to implement resize policy
*/
void _resize(DA *d, int size) {

    /*
    if (size > d->size) {


    } elif
    */

}

void _copy_forwards(DA *d, int i) {
    ;
}

void _copy_backwards(DA *d, int i) {
    ;
}


void insert_last(DA *d, int val) {
    int k = d->numI + 1;
    _resize(d, k);
    d->arr[k] = val;
    d->numI += 1;
}

int delete_last(DA *d) {
    int last = d->arr[d->numI - 1];
    d->arr[d->numI - 1] = -1;
    d->numI -= 1;
    _resize(d, d->numI);
    return last;
}


/*
    Simple test debugging code
*/

int main()  {
    /* Check creates empty array*/
    DA *d = createDA();
    displayDA(d);
    freeDA(d);

    /* Check init correctly */

    /* Check numS doubling works*/

    /* Check numS halving works */
    return 0;
}