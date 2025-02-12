#include <stdio.h>

int main(void){
    int x = 5;
    if(x == 2)
    {
        printf("x IS EQUAL TO 2 !!\n");
    }//The semicolon is inside the curly bracket here
    else if(x == 3){
        printf("x IS EQUAL TO 3 !!\n");
    }
    else{
        printf("x IS not EQUAL TO 2 or 3\n");
    }
    printf("if done!\n");
    return 0;
}