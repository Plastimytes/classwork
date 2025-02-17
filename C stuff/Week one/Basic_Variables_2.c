#include <stdio.h>

//Declaring multiple variables

int main(void){
    int position= 10; //variable initialization//Can also be done as int position=10;
    int x, y, z; //declare variables x, y and z ie; three integers
    x=2;
    y=5;
    z=-3;

    //float
    float mynum= 3.3455345;

    //double(Stores decimals with higher degree of percision because they use more bits to store values)
    double mydouble= 3.3455345;

    //car(Stores character values)
    char c= 113;
    char t= 'Y';

    printf("position: %d\n", position);
    printf("x: %d,y: %d, z: %d\n", x,y,z);//% means expect another argument and d means its an integer therefore expect three integers as values
    printf("Float: %lf\n", mynum); //%lf means expect a floating point value
    printf("double: %lf\n", mydouble);
    printf("C: %c\n", c);//%c means expect a character value
    printf("t: %c\n", t);

    return 0;
}

//unsigned int ,eans 0 to +ve range of numbers only
//short int means it going to take up less bits(less memory)
