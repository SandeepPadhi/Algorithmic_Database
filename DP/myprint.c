/*
The important insight here is that address of the variable gives address of the end of that memory and not the start of that memory..
it int follow a char,then we must add the size of int to the address of char.
if char * follows a char,then we must add the size of char * to get the address of that char *.

Again ,remember that address that you will be getting is the end of the memory address and not the start..
*/
#include <stdio.h>
#include <stdbool.h>

int try(const char *,int ,...);
int main()
{
    printf("Hello World");
    try("Sandeep",22,4,6);
    return 0;
}

int try(const char* N,int a,...)
{
    bool stackdir=true;  // Mouli: This flag means stackDir is Down ... if it is true
    //const char** addr = (char *)&N;
    int cnt;
    //int * param;
    if ((void *)&stackdir > (void *)&N)   // Mouli: I changed it from < to > because now it means stack grows up
    {
        stackdir=false;

    }

    printf("\nstackdir value is %d", stackdir);   // Mouli: I added it to check the value of the flag

    if (stackdir)
    {
        //printf("\n name is %s true",*addr);

        //cnt = *(int *)((void *)addr + sizeof(int *));
        //addr=(int *)&cnt;
        printf("\ncnt:%d",cnt);

        /*
        for(int i=0;i<cnt;i++)
        {
            addr= (int*)((void *)addr + sizeof(int *));
            fputs("param 1",stdout);
            //fputs(i+1,stdout);fputs(*addr);


        }
        */
    }
    else{
        /*
        printf("\n name is %s false",N);
        printf("\naddr of N: %p",(void *)&N);
        printf("\naddr of a:%p",(void *)&a);
        printf("\nsize of char pointer: %lu"     ,sizeof(char *));
        printf("\nsize of char N: %lu"     ,sizeof(N));
        printf("\nsize of int variable %lu",sizeof(cnt));
        printf("\nsize of int %lu",sizeof(int));
        printf("\nsize of  unsigned: %lu"     ,sizeof(unsigned));
*/
        cnt = *((int *)((void *)&N - sizeof(unsigned)));
        printf("\ncnt:%d",cnt);
        cnt = *((int *)((void *)&N - sizeof(const char *)));
        printf("\ncnt:%d",cnt);


        /*
        addr=(int *)&cnt;
        for(int i=0;i<cnt;i++)
        {
            addr= (int*)((void *)addr - sizeof(int *));
            fputs("param ",stdout);


        }
        */

    }
    return 6;

}
