#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Text: ");

    int num_words = 1;
    int num_sentences = 0;
    int num_letters = 0;

    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (s[i] == ' ')
        {
            num_words++;
        }
        if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            num_sentences++;
        }
        if (isalpha(s[i]))
        {
            num_letters++;
        }
    }

    float L = (num_letters / (float) num_words) * 100;
    float S = (num_sentences / (float) num_words) * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
