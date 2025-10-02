#include <stdio.h>

int main(int argc, char *argv[])
{
    #ifdef TEST
    printf("TEST is defined\n");
    #else 
    printf("TEST is not defined\n");
    #endif

    #if VALUE==0
    printf("VALUE is 0\n");
    #elif VALUE==1
    printf("VALUE is 1\n");
    #elif VALUE==2
    printf("VALUE is 2\n");
    #elif VALUE==3
    printf("VALUE is 3\n");
    #endif
}
