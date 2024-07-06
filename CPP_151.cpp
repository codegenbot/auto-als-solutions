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
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    for(int i=0; i<n; i++) {
        double num;
        cout << "Enter element " << i+1 << ": ";
        cin >> num;
        lst.push_back(num);
    }
    long long odd_sum = double_the_difference(lst);
    cout << "The sum of squares of odd elements is: " << odd_sum;
    return 0;
}