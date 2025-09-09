//Scanf!! The man weve all been waiting for is function that accepts input from the user
//Scanf is typically reading from stattered input which is the terminal. It can also be a file
#include <stdio.h>
int main(void)
{
    int n =0;
    printf("Enter a number: ");
    scanf("%d",&n);//"scanf" is the first thing,"%d" is to tell the code to expect an integer and "&n" is telling the code where to store the integer(Into the varaiable n)
    printf("n: d\n", n);
    return 0;
}

//its the same order for char, float and doubles