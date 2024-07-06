#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

int sum_squares(vector<float> lst){
    int total = 0;
    for(float x : lst){
        int ceil_x = ceil(x);
        total += (ceil_x * ceil_x);
    }
    return total;
}