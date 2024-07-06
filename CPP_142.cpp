#include<stdio.h>
#include<vector>
using namespace std;
int sum_squares(vector<int> lst){
    int total = 0;
    for(int i=0; i<lst.size();i++){
        if(i%3==0 && i%4!=0) // Square the integer entry if its index is a multiple of 3
            total += pow(lst[i],2);
        else if(i%4==0 && i%3!=0) // Cube the integer entry if its index is a multiple of 4 and not a multiple of 3
            total += pow(lst[i],3);
    }
    return total;
}