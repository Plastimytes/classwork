#include <stdio.h>
int main(void){
    int x=5;
 
    if (x<4)printf("1st cond!\n");
    else if(x<5)printf("2nd cond!\n");
    else if(x<6)printf("3rd cond!\n");
    else if(x<7)printf("4th cond!\n");
    else printf("else case!\n");

    printf("If done\n");

    return 0;
    
 }