#include <stdio.h>


void main(){
    printf("Hello world\n");
    printf("Hello Magezi\n");

    int a=3;int b=5; int c=52; int d=a+c+b;

    printf("%d\n", d);

    if(c<10){printf("Low");}
    if(c>10){printf("High");}

    //USER INPUT
    printf("Enter a number:");
    scanf("%d",&d);
    ///Void doesnt require return 0;
}