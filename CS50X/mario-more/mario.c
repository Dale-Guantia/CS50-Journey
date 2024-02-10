#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // TODO: Build the pyramids
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height; j++)
        {
            if (i+j < height - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("  ");
        for (int k = 0; k < i+1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
