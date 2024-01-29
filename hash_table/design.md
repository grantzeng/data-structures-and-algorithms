# What does a hash table need to offer?

- (From 6.006 Lec 4):
    - container operations: `build(X)`
    - static operations: `find(k)`
    - Dynamic operations: `insert(x)`, `delete(k)`
    - Order operations:`find_min()`, `find_max()`, `find_prev(k)`, `find_next(k)`
- (Alternative interface from COMP2521 23T3)
```C
// Interface to the hash table module
#ifndef HASH_TABLE_H
#define HASH_TABLE_H

#include <stdbool.h>

typedef struct hashTable *HashTable;

HashTable HashTableNew(void);

void HashTableFree(HashTable ht);

void HashTableInsert(HashTable ht, int key, int value);

void HashTableDelete(HashTable ht, int key);

bool HashTableContains(HashTable ht, int key);

int HashTableGet(HashTable ht, int key);

int HashTableSize(HashTable ht);

void HashTableShow(HashTable ht);

#endif
```
- so if I'm doing a minimal Python implementation to just get the gist of the algorihm it's: insert a key:value, delete a key, get value with a key, check key exists

- Collision resolution:
    - implement separate chaining
    - implement linear probing
    - implement double hashing

- a hash function
    - a bad hash function
    - a good hash function


### Summary of features I want to offer
crude hashtable that inserts integers

- `insert(x)`
- `delete(x)`
- `search(k)`: return None, a linked list or an int
- a hash function
    - implement an easy to implement but crap one (then implement a better one) - just do modulus
- collision resolution
    - with chaining (because easier to analyse)

optional extras:
- make the table resize dynamically
- implement a better hash function
- order operations