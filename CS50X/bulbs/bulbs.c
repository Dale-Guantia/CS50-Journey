#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string message = get_string("Message: ");

    for (int i = 0; i < strlen(message); i++)
    {
        unsigned char byte = message[i];
        int binary[BITS_IN_BYTE];
        int quotient = byte;
        int remainder;

        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            remainder = quotient % 2;
            binary[j] = remainder;
            quotient /= 2;
        }

        for (int k = 7; k >= 0; k--)
        {
            print_bulb(binary[k]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
