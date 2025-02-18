#include <stdio.h>


///  Exact type doesn't really matter cause its almost exactly the same

int main(void)
{
    int myarray[] = {2,3,6,1,8,5,10,34,24};

    //Finding the minimum number in the array
    int min;
    min = myarray[0]; //Assume that the first thing in tthe array is the smallest thing in the array..For now
    for (int i = 0; i < 9; i++)///9 is the number of things in the array
    {
        if (myarray[i]< min) min = myarray[i];//if my array at i is less than min, then make min equal to myarray at i
    }
    
    printf("Minimum: %d\n", min);
    return 0;
}