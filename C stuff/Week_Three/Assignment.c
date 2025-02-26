#include <stdio.h>


void main(){
    
    int a=0;int b=0;

    //User input
    printf("Enter a: \n");
    scanf("%d",&a);
    printf("Enter b: \n");
    scanf("%d",&b);
    int c=a+b;
    printf("%d\n", c);

    if(c<10){
        for(int i=0; i<10; i++){printf("Below 10\n");}}
    if(c>10){
        for(int i=0; i<10; i++){printf("Above 10\n");}}

   
}