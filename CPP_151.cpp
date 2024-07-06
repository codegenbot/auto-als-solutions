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
    std::vector<float> lst = {1.5f, 2.3f, 3.4f};
    float odd_sum = double_the_difference(lst);
    return 0;
}