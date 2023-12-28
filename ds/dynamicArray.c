/*

    Partial C implementation of the dynamic array in Recitation 2.
    Written for revising practical aspects of COMP2521.

    TODO:
    - Think about testing (many array bounds type issues)
*/

#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

#define SCALE_FACTOR 2

typedef struct {
    int *arr;   // Pointer to a static array
    int  len;   // Number of items in array/array usage
    int  cap;   // Total allocated memory size/max size of curr static array

} DA;

/*

    Helper functions for memory management

*/
void displayDA(DA *d) {
    printf("\nOccupied size: %d\n", d->len);
    printf("[ ");
    for (int i = 0; i < d->len; i++) {
        printf("%d ", d->arr[i]);
    }
    for (int i = d->len; i < d->cap; i++) {
        printf("X ");
    }
    printf("]\n");
    printf("Allocated size: %d\n\n", d->cap);
}

DA *createDA() {

    DA *d = malloc(sizeof(DA));
    assert(d != NULL);

    d->arr = (int *)malloc(sizeof(int));
    d->len = 0;
    d->cap = 1;

    return d;
}

void freeDA(DA *d) {
    free(d->arr);
    free(d);
}


/*

    More memory management

*/
void _resize(DA *d, int size) {

    int cap = d->cap;

    if (size > d->cap) {
        // Double array
        cap = d->cap * SCALE_FACTOR;
    }  else if (size < ( d->cap / SCALE_FACTOR ) ) {
        // Halve array
        cap = d->cap / SCALE_FACTOR;
    } else {
        // Enough capacity, do nothing
        return;
    }

    int *new = (int *)malloc(cap * sizeof(int));
    for (int i = 0; i < d->len; i++) {
        new[i] = d->arr[i];
    }

    free(d->arr);

    d->arr = new;
    d->cap = cap;
}

void _copy_forwards(DA *d, int idx) {
    int len = d->len + 1;
    _resize(d, d->len + 1);

    for (int i = len; i > idx; i--) {
        d->arr[i] = d->arr[i - 1];
    }
}

void _copy_backwards(DA *d, int idx) {
    for (int i = idx; i < d->len - 1; i++) {
        d->arr[i] = d->arr[i + 1];
    }
    _resize(d, d->len - 1);
}

/*

    Static operations

*/

int get_at(DA *d, int idx) {
    ;
}

void set_at(DA *d, int idx, int val) {
    ;
}


/*

     Dynamic operations

*/
void insert_at(DA *d, int val, int idx) {
    assert(idx < d->len && idx >= 0);

    _copy_forwards(d, idx);
    d->arr[idx] = val;
    d->len += 1;
}

int delete_at(DA *d, int idx) {
    assert(idx < d->len && idx >= 0);

    int val = d->arr[idx];
    _copy_backwards(d, idx);
    d->len -= 1;
    return val;
}

void insert_last(DA *d, int val) {
    int len = d->len + 1;
    _resize(d, len);
    d->arr[len - 1] = val;
    d->len += 1;
}

int delete_last(DA *d) {
    int last = d->arr[d->len - 1];
    d->arr[d->len - 1] = -1;
    d->len -= 1;
    _resize(d, d->len);
    return last;
}

void insert_first(DA *d, int val) {
    insert_at(d, val, 0);
}

int delete_first(DA *d) {
    int elem = delete_at(d, 0);
    return elem;
}


/*
    Simple print debugging "tests"
*/

int main()  {
    // Check initialisation works
    DA *d = createDA();
    displayDA(d);
    freeDA(d);

    // Check resizing works
    d = createDA();
    for (int i = 0; i < 100; i++) {
        insert_last(d, i);
    }

    for (int i = 0; i < 100; i++) {
        delete_last(d);
    }

    for (int i = 0; i < 100; i++) {
        insert_last(d, i);
    }

    for (int i = 0; i < 100; i++) {
        delete_last(d);
    }

    displayDA(d);
    freeDA(d);

    // Check insert/delete at an index works
    d = createDA();

    for (int i = 0; i < 4; i++) {
        insert_last(d, i);
    }
    displayDA(d);
    delete_at(d, 3);
    displayDA(d);
    delete_at(d, 2);
    displayDA(d);
    insert_at(d, 9999, 0);
    displayDA(d);
    insert_at(d, 9998, 0);
    displayDA(d);
    delete_at(d, 0);
    displayDA(d);


    return 0;
}