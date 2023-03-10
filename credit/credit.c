#include <cs50.h>
#include <stdio.h>

int sumDigits(int n)
{
    int lastNumber = n % 10;
    int firstNumber = n / 10;
    return lastNumber + firstNumber;
}
//PASS

int main(void)
{
    long num = get_long("Number: ");
    int noOfDigits = 0;
    int multiplied = 0;
    int notMultiplied = 0;
    int firstNumber = 0;
    int secondNumber = 0;
    int i = 0;//why

    while (true)
    {
        noOfDigits++;

        if (num < 10)
        {
            firstNumber = num;
            if (i % 2 == 1)
            {
                num = num * 2;
                if (num > 9)
                {
                    num = sumDigits(num);
                }
                multiplied += num;
            }
            else if (i % 2 == 0)
            {
                notMultiplied += num;
            }
            break;
        }
        if (num < 100)
        {
            secondNumber = num % 10;
        }
        // CHECKING
        int digit = num % 10;
        num = num / 10;

        if (i % 2 == 1)
        {
            digit = digit * 2;
            if (digit > 9)
            {
                digit = sumDigits(digit);
            }
            multiplied += digit;
        }
        else if (i % 2 == 0)
        {
            // if(digit > 9)
            // {
            //     digit = sumDigits(digit);
            // }
            notMultiplied += digit;
        }
        i++;

    }

    int sum = multiplied + notMultiplied;
    int firstTwoDigits = (firstNumber * 10) + secondNumber;
    if (sum % 10 == 0)
    {
        if (firstNumber == 4)
        {
            if (noOfDigits == 13 || noOfDigits == 16)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (firstTwoDigits == 34 || firstTwoDigits == 37)
        {
            if (noOfDigits == 15)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (firstTwoDigits == 51 || firstTwoDigits == 52 || firstTwoDigits == 53 || firstTwoDigits == 54 || firstTwoDigits == 55)
        {
            if (noOfDigits == 16)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }

    }
    else
    {
        printf("INVALID\n");
    }
}