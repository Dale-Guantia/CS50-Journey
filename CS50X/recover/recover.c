#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BYTE_BLOCK 512

typedef uint8_t BYTE;

void argCountChecker(int argc);
void fileChecker(FILE *file);
int jpegChecker(BYTE buffer[]);

int main(int argc, char *argv[])
{
    argCountChecker(argc);
    FILE *raw = fopen(argv[1], "r");
    fileChecker(raw);

    BYTE buffer[BYTE_BLOCK];

    char filename[8];
    FILE *image;
    int count = 0;

    while (fread(buffer, BYTE_BLOCK, 1, raw) == 1)
    {
        if (jpegChecker(buffer) == 1)
        {
            if (count != 0)
            {
                fclose(image);
            }
            sprintf(filename, "%03i.jpg", count++);
            image = fopen(filename, "w");
            fwrite(buffer, BYTE_BLOCK, 1, image);
        }

        else if (count > 0)
        {
            fwrite(buffer, BYTE_BLOCK, 1, image);
        }
    }
    fclose(raw);
    fclose(image);
}

void argCountChecker(int argc)
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        exit(1);
    }
}

void fileChecker(FILE *file)
{
    if (file == NULL)
    {
        printf("File could not be opened.\n");
        exit(1);
    }
}

int jpegChecker(BYTE buffer[])
{
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        return 1;
    }
    return 0;
}
