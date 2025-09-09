#include <stdio.h>

int main(void){
    printf("Helllo world\n");
    printf("Another line of text\n");
    printf("\tThis is the end\n");
    printf("double qoute: \"\n");
    printf("\\");

    printf("int: %d\n");//for integers and %d is a place holder for integers
    printf("int: %d\n", 4);
    int x =5;
    printf("int: %d\n", x);
    printf(" %d, %d, %d\n", x, x+1, x+2);

    char c = 'Q';//For characters single qoutes are better
    printf("C: %C\n", c);

    double y = 4.453726;
    printf("double: %lf\n", y);

    float z= 2.345;
    printf("z; %lf\n", z);//Best to use %lf

    char str[] ="A string of yarn \n";//"\n" can go up here of in print f in this case
    printf("The words are: %s", str);

    //Under formating optons
    printf("|||%d|||\n", 5);
    //width
    printf("|||%10d|||\n", 5);

    //flag(left align)
    printf("|||%-10d|||", 5);

    //dot precision
    printf("|||%8.2f|||\n", y);//"8" right aligns but 8 measures and "2" is the number of decimal places
    printf("|||%-12.3f|||\n", y);//"8" 
    return 0;
}
//printf is th function and Hello world is the string
//\t creates an indentation on the printf statement
//printf(" \"); is wrong
//Alot of tings in C have to be done ourselves e.g \n to create a new line on the teerminal(To begin on the new line)

//Formatting options
//E.g Flags, Width etc
