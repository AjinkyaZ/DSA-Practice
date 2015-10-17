#include <stdio.h>

void main()
{
printf("Hello World\n");
int a = 10;
int *p;
p = &a;
printf("val of a --> %d\n", a);
printf("val of ptr to a i.e p --> %d\n", p);
printf("addr of p --> %d\n", &p);
printf("addr of var at ptr p --> %d\n", *p);
}

