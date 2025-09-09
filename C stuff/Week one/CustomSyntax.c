#include <stdio.h>  // Preprocessor directive to include standard input-output library

// Function declaration
void myFunction(); // A simple function declaration

// The main function - execution starts here
int main() {
    printf("Hello, World!\n"); // Print a message to the console. It wil be the firts one to appear
    myFunction(); // Call the custom function
    return 0; // Return 0 to indicate successful execution
}

// Function definition
void myFunction() {
    printf("Lo and BEHOLD!!!! A custom function.\n"); // Print another message
}

///Notes
//'int main ()' is the entry point of every C program
//return 0 indicates the that the program has executed successfully.
//The function 'myFunction' is defined after the 'main' function. It contains its own statements, which will be executed when the function is called.