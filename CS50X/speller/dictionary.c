// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_num = hash(word);

    node *ptr = table[hash_num];

    while(ptr != NULL)
    {
        if(strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict_file = fopen(dictionary, "r");

    if(dict_file == NULL)
    {
        return false;
    }

    char str[LENGTH + 1];
    while(fscanf(dict_file, "%s", str) != EOF)
    {
        node *temp = malloc(sizeof(node));

        if(temp == NULL)
        {
            return false;
        }

        strcpy(temp->word, str);

        int hash_num = hash(str);

        if(table[hash_num] == NULL)
        {
            temp->next = NULL;
        }
        else
        {
            temp->next = table[hash_num];
        }

        table[hash_num] = temp;

        word_count += 1;
    }

    fclose(dict_file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

void free_node(node *n)
{
    if(n->next != NULL)
    {
        free_node(n->next);
    }
    free(n);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for(int i = 0; i < N; i++)
    {
        if(table[i] != NULL)
        {
            free_node(table[i]);
        }
    }
    return true;
}
