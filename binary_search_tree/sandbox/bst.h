/*
	BST implementation from 2521_23T3

*/

#ifndef BST_H
#define BST_H

#include <stdbool.h>

struct node {
	int val;
	struct node *left;
	struct node *right;
};

struct node *bstInsert(struct node *tree, int val);

bool bstSearch(struct node *tree, int val);

struct