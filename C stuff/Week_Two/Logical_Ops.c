#include <stdio.h>

int main(void){
    int x=5;
    if(x>5) printf("OK!\n");
    else printf("Not OK!\n");

    ///AND and OR operators(&& and ||)

    int year = 23;
    int price = 22000;

    if (year >= 2019 || price <= 20000)printf("OK!\n");
    else printf("Not Ok!\n");

    //NOT(!) operator
    if(!(x<5)) printf("OKAY!\n");
    else printf("Not OKAY!\n");
    return 0;
}

