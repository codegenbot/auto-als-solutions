#include <vector>
#include <cmath>

int main() {
    std::vector<float> lst = {1.0f, 2.0f, 3.0f, 4.0f};
    float odd_sum;
    assert(double_the_difference(lst) == odd_sum);
    return 0;
}

long long double_the_difference(std::vector<float> lst){
    long long sum = 0;
    for(auto x : lst){
        if(int(x) > 0 && int(x) == int(x)){
            sum += pow(int(x), 2);
        }
    }
    return sum;
}