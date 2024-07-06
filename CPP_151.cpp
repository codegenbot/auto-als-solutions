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

int programEntry() {
    vector<double> lst;
    for (double num : {1.5, 2.5, -3.4, 4.7}) {
        lst.push_back(num);
    }
    long long odd_sum = 0; 
    assert(double_the_difference(lst) == odd_sum); 
    return 0;
}

int main() {
    programEntry();
    return 0;
}