```c++
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
    vector<double> lst;
    for(double i=1.5; i <= 4.7; i+=0.5) {
        lst.push_back(i);
    }
    long long odd_sum = double_the_difference(lst);
    cout << odd_sum;
    return 0;
}