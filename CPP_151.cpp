#include <vector>
#include <cmath>
#include <iostream>

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
    vector<double> lst({1.0, 2.0, -3.0, 4.0});
    long long odd_sum = double_the_difference(lst);
    cout << odd_sum;
    return 0;
}