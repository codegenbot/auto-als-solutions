#include <vector>
#include <cmath>

int main() {
    std::vector<float> lst = {1.2f, 3.4f, 5.6f};
    float odd_sum = 0;
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