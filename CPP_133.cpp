#include <vector>
#include <cmath>

int sum_squares(std::vector<float> lst){
    int sum = 0;
    for(float i : lst){
        int ceil_i = std::ceil(i);
        sum += std::pow(ceil_i,2);
    }
    return sum;

}

int main() {
    assert(sum_squares({-1,1,0})==2);
    return 0;
}