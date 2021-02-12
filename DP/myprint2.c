#include <stdio.h>
#include <stdbool.h>

int myprint(char *,...);

int main()
{
myprint("Sandeep",24,50,10);
return 0;
}

int myprint(char *N,...)
{
int* nptr;
char* cptr;
int num;
bool stackdir=false;//stackaddress is

if ((void *)&stackdir< (void *)&N)
{
    stackdir=true;//stackdir is at low address then local variables

}
printf("\nstackdir is %d",stackdir);
printf("\naddress of nptr is %p",&nptr);
printf("\naddress of N is %p",&N);
//printf("\naddress of a is %p",&a);

if(stackdir)
{

printf("\nName is %s",N);
nptr = (int *)((void* )&N + sizeof(int));
printf("\nage is %d",*nptr);

}
else{

printf("\nstackdir is %d",stackdir);
printf("\nName is %s",N);

printf("\nbackward");
for(int i=1;i<100;i++)
{
nptr = (int *)((void* )&N - (unsigned)i);
//printf("\nnptr is %p",nptr);
printf("\nage is %d",*nptr);
}
printf("\n\n");
printf("\nforward");
for(int i=1;i<50;i++)
{
nptr = (int *)((void* )&N + (unsigned)i);
//printf("\nnptr is %p",nptr);
printf("\nage is %d",*nptr);
}

}

return 0;
}

