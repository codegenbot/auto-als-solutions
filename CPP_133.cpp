#include <vector>
#include <cmath>

int sum_squares(std::vector<float> lst){
    int total = 0;
    for(float x : lst){
        total += pow(x,2);
    }
    return total;
}