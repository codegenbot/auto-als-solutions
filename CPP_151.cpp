#include <vector>
#include <cmath>

long long double_the_difference(std::vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && floor(num) == num) { // check if number is positive and integer
            sum += pow(num, 2);
        }
    }
    return sum;
}

int main() {
    std::vector<float> lst;  
    int odd_sum = 0; 

    assert(double_the_difference(lst) == odd_sum);

    return 0;
}