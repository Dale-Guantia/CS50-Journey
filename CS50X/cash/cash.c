#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int input;
    do
    {
        input = get_int("Change owed: ");
    }
    while (input < 0);

    return input;
}

int calculate_quarters(int cents)
{
    int num_quarters = 0;

    for (int i = cents; i >= 25; i -= 25)
    {
        num_quarters++;
    }

    return num_quarters;
}

int calculate_dimes(int cents)
{
    int num_dimes = 0;

    for (int i = cents; i >= 10; i -= 10)
    {
        num_dimes++;
    }

    return num_dimes;
}

int calculate_nickels(int cents)
{
    int num_nickels = 0;

    for (int i = cents; i >= 5; i -= 5)
    {
        num_nickels++;
    }

    return num_nickels;
}

int calculate_pennies(int cents)
{
    int num_pennies = 0;

    for (int i = cents; i >= 1; i -= 1)
    {
        num_pennies++;
    }

    return num_pennies;
}
