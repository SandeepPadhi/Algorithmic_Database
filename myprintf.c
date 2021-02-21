/******************************************************************************
Name:Sandeep Padhi                                      Date:21/02/2021
ID:MCS20006
Title:Custom printf Function                 
*******************************************************************************/

#include <stdio.h>
#include<stdarg.h>
#include<string.h>
#include<stdbool.h>

int myprintf(char *,...);
void print_int(long);
void print_float_double(float,int);
int main()
{   
    myprintf("My name is %s . I am %d years old. My height is %lf cm","Sandeep",24,132.23);
    myprintf("\nI am in %dst year Mtech",1);
    myprintf("\nTodays temperature is %d degree",24);
}


//This function prints int
void print_int(long n)
{
    // If number is smaller than 0, put a - sign and
    // change number to positive
    if (n < 0) {
        putchar('-');
        n = -n;
    }
 
    // If number is 0
    if (n == 0)
        putchar('0');
 
    // Remove the last digit and recur
    if (n/10)
        print_int(n/10);
 
    // Print the last digit
    putchar(n%10 + '0');
}

//This function prints float and double
void print_float_double(float x,int type)
{
    int d;
    int p=2;//precision-till third decimal place
    
    if (x < 0) {
        putchar('-');
        x = -x;
    }
 
    // If number is 0
    if (x == 0)
    {
        putchar('0');
        //return;
    }
    
    if (type==2)//type2-double,default - float
    {
        p=6;
    }
    d=x;

    print_int(d);
    putchar('.');
    x=x-d;
    while(p--)
    {
        x=x*10;
        d=x;
        putchar(d+'0');
        x-=d;
    }
    
    
    
}

//custom printf function
int myprintf(char* S,...)
{
    //char input[1000];
    //char *p=S;
    va_list arguments;
    int i=0;
    va_start(arguments,S);

    while(i<strlen(S)){
        //putchar(S[i]);
        if (S[i]=='%')
        {   bool flag=false;
            if (i+1<strlen(S))
            {
                int j=i+1;
                bool flag=false;
                if (S[j]=='d' || S[j]=='i')
                {   
                    print_int(va_arg(arguments,int));
                }
                else if(S[j]=='c')
                {
                    putchar(va_arg(arguments,char));
                }
                else if (S[j]=='f')
                {  
                    float num=(float)va_arg(arguments,double);
                    print_float_double(num,1);
                    
                }
                else if(S[j]=='l' && S[j+1]=='f')
                {
                    print_float_double(va_arg(arguments,double),2);
                    i+=3;
                    continue;
                }
                else if(S[j]=='s')
                {   int k=0;
                    char *str=va_arg(arguments,char *);
                    while(k<strlen(str)){
                        putchar(str[k]);
                    k++;
                    }
                }
                else{
                    putchar('%');
                    flag=true;
                }
                
            }
            
            if (flag)
            {
                i++;
            }
            else{
                i+=2;
            }
            
            
        }
        else if(S[i]=='\n')
        {
            putchar('\n');
            i+=1;
        }
        else{
            putchar(S[i]);
            i+=1;
        }
    }
    
    
    
    
}


/*
Output:
My name is Sandeep . I am 24 years old. My height is 132.229995 cm
I am in 1st year Mtech
Todays temperature is 24 degree

*/

