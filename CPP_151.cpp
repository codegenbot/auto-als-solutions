#include <vector>
#include <cmath>
#include <cassert>
using namespace std;

long long double_the_difference(vector<double> lst) {
    long long sum = 0;
    for (double num : lst) {
        if (num > 0 && floor(num) == num) {
            sum += pow(num, 2);
        }
    }
    return sum;
}

int main() {
    vector<double> lst({1.5, 2.5, -3.4, 4.7});
    long long odd_sum; 
    odd_sum = double_the_difference(lst); 
    assert(odd_sum == 0); 
    return 0;
}