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


# Resizing policy
> 2024-01-30

Most of the discussion in CLRS + 6.006 centres on what makes a good hash function, than resizing policy.

I think for argument's sake just implement it as table doubling + table halving. Then with a better hash function, we can avoid e.g. the isssue of e.g. inserting multiple of e.g. 10, landing all in the same slot that is capable of spreading elements out. modulo hash bad




# Current solutions
> Current use of a chain should really be a set interface on top of a linked list with testing, the current implementation is just something I hacked up on the spot

Things to implement:
- modulo hash, no resizing, chaining (done)
- universal hash, table doubling, chaining (done, 2024-01-30)
- universal hash, table doubling, linear probe
- modulo hash, table doubling with rouding up to nearest prime, chaining (might not bother with this one)
- modify the fill ratio and see how this affects performance

Can we write some code to compare different implementations







