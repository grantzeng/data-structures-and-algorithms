/*
    Singly linked list C implementation of code in Recitation 2.
    - Implements sequence interface

    TODO:
    - This implementation is leaking memory and I haven't written tests for edge cases. Come back to do it later.


*/

#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

struct node {
    int data;
    struct node *next;
};
typedef struct node Node;

typedef struct {
    Node *head;
    int size;
} LL;


/*
    
    Memory management helpers

*/

Node *createNode(int val) {
    Node *node = malloc(sizeof(Node));
    node->data = val;
    node->next = NULL;
    return node;
}

void freeNode(Node *node) {
    free(node);
}

LL *createLL() {
    LL *new = malloc(sizeof (LL));
    assert (new != NULL);
    new->size = 0;
    new->head = NULL;
    return new;
}

void freeLL(LL *ll) {
    Node *curr = ll->head;
    Node *nxt;

    while (curr != NULL) {
        nxt = curr->next;
        free(curr);
        curr = nxt;
    }

    free(ll);
}

void displayLL(LL* ll) {
    
    assert(ll != NULL);
    

    Node *curr = ll->head;

    while (curr != NULL) {
        printf("%d -> ", curr->data);
        curr = curr->next;
    }

    printf("X\n");
}

/*

    Helpers
    - _succ is just for implementing recursive traversal of the linked list
      but we could have just written a loop

      Does not handle case where i > number of elements in the list. User shouldn't abuse it that's all.
*/

Node *_succ(Node *n, int i) {
    if (i == 0) {
        return n;
    }

    assert(n != NULL);
    Node *res = _succ(n->next, i - 1);
    return res;
}


/*

    Static operations

*/
int get_at(LL *ll, int idx) {
    Node *node = _succ(ll->head, idx);
    return node->data;
}

void set_at(LL *ll, int idx, int val) {
    Node *node = _succ(ll->head, idx);
    node->data = val;
}


/*

    Dynamic operations

*/

void insert_first(LL *ll, int val) {
    Node *node = createNode(val);
    node->next = ll->head;

    ll->head = node;
    ll->size++;
}

int delete_first(LL *ll) {

    assert(ll->head);

    Node *nxt = ll->head->next;
    int val = ll->head->data;
    free(ll->head);

    ll->head = nxt;
    ll->size--;

    return val;
}


void insert_at(LL *ll, int idx, int val) {
    if (idx == 0) {
        insert_first(ll, val);
        return;
    }

    Node *prev = _succ(ll->head, idx - 1);
    Node *new = createNode(val);
    new->next = prev->next;
    prev->next = new;

    ll->size++;
}

int delete_at(LL *ll, int idx) {
    if (idx == 0) {
        return delete_first(ll);
    }

    Node *prev = _succ(ll->head, idx - 1);
    Node *targ = prev->next;

    int val = targ->data;
    prev->next = targ->next;
    free(targ);
    ll->size--;
    return val;

}

void insert_last(LL *ll, int val) {
    // insert_at(ll, ll->size - 1, val);
    insert_at(ll, ll->size, val);
}

int delete_last(LL *ll) {
    return delete_at(ll, ll->size - 1);
}

// Simple debugging tests
int main() {
    // Create delete empty
    LL *ll = createLL();
    displayLL(ll);
    freeLL(ll);

    // Create insert delete (checking no memory leaks
    ll = createLL();
    for (int i = 0; i <= 5; i++) {
        insert_first(ll, i);
        displayLL(ll);
    }

    for (int i = 0; i <= 5; i++) {
        delete_first(ll);
        displayLL(ll);
    }
    freeLL(ll);

    // Create/delete at a particular index
    ll = createLL();
    for (int i = 0; i <= 5; i++) {
        insert_first(ll, i);
    }
    displayLL(ll);

    for (int i = 0; i <= 4; i++) {
        delete_at(ll, 1);
        displayLL(ll);
    }

    freeLL(ll);

    // Try insert_last and delete_last
    ll = createLL();

    for (int i = 0; i <= 5; i++) {
        insert_first(ll, i);
    }

    displayLL(ll);
    for (int i = 0; i <= 5; i++) {
        if (i % 2) {
            insert_last(ll, i);
        } else {
            delete_last(ll);
        }
        displayLL(ll);
    }

    free(ll);

}

