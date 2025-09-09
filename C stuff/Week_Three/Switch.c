#include <stdio.h>
/// Similar to if else

int main(void)
{
    int num = 1;
    switch (num)
    {
        case 1: 
        printf("Case 1 \n ");
        if(1==1) printf("if\n");
        break;

        case 2: 
        printf("Case 2 ");
        break;
    }
    printf("Below switch statements\n");
    return 0;
}