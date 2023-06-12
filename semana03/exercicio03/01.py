#include <stdio.h>
#include <unistd.h>

#exercio 1
int main()
{
    printf("The process ID id %d\n", (int) getpid());
    printf("The parent process ID is %d\n", (int) getppid());
    return 0;
}

