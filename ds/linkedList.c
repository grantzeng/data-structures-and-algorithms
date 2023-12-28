/*
    Singly linked list C implementation of code in Recitation 2.
    - Implements sequence interface




*/

#include <stdlib.h>
#include <assert.h>
#include <stdio.h>

typdef struct {
    int data;
    Node *next;
} Node;

typedef struct {
    Node *head;
    int size;
} LL;


/*
    
    Memory management helpers

*/

void createLL() {
    ;
}

void freeLL() {
    ;
}

void displayLL(LL* l) {
    ;
}

/*

    Helpers
    - _succ is just for implementing recursive traversal of the linked list
      but we could have just written a loop
*/

Node *_succ(Node *n, int i) {
    ;
}


/*

    Static operations

*/
int get_at(LL *l, int idx) {
    ;
}

int set_at(LL *l, int idx, int val) {
    ;
}


/*

    Dynamic operations

*/

void insert_first(LL *l, int val) {
    ;
}

int delete_first(LL *l) {
    ;
}

void insert_last(LL *l, int val) {
    ;
}

int delete_last(LL *l) {
    ;
}

void insert_at(LL *l, int idx, int val) {
    ;
}

int delete_at(LL *l, int idx) {
    ;
}

