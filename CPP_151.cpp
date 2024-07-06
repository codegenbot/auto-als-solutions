#include <vector>
#include <cmath>
#include <cassert>
using namespace std;

long long double_the_difference(vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && floor(num) == num) {
            sum += pow(num, 2);
        }
    }
    return sum;
}

int main() {
    vector<float> lst = {1.5f, 2.5f, -3.4f, 4.7f};
    long long odd_sum = 0; 
    odd_sum = double_the_difference(lst); 
    assert(odd_sum == 0); 
    return 0;
}