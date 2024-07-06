```cpp
// Here is the completed code:
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