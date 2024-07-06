#include <vector>
#include <cmath>

long long double_the_difference(std::vector<float> lst){
    long long sum = 0;
    for(auto x : lst){
        if(int(x) > 0 && int(x) == int(x)){
            sum += pow(int(x), 2);
        }
    }
    return sum;
}

int main() {
    std::vector<float> lst = {1.5, 3.8, 4.9};
    float odd_sum = 16.0;
    assert(double_the_difference(lst) == odd_sum);
    return 0;
}