#include <stdio.h>
#include <stdlib.h>

FILE* f;

int main(int argc, char** argv)
{
    if (argc != 2) { fprintf(stderr, "usage: p1 <input_file_path>\n"); exit(1); }

    f = fopen(argv[1], "r");

    printf("Reading from file %s\n", argv[1]);

    int num;
    int prev = -1;

    int total = 0;

    for(int i = fscanf(f, "%d", &num); i != EOF; i = fscanf(f, "%d", &num)) {

        if (prev != -1) { 
            char* output = num > prev ? "INC" : "DEC";
            if (num > prev) total++;
            printf("%d <%s>\n", num, output);
        }
        prev = num;
    }

    printf("Total increases: %d\n", total);
    fclose(f);
    return 0;
}
