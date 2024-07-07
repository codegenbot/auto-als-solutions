#include <iostream>
#include <vector>
using namespace std;

long long double_the_difference(vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && floor(num) == num) { 
            if (num % 2 != 0) { 
                sum += pow(num, 2); 
            }
        }
    }
    return sum;
}

int main() {
    vector<float> lst;
    long long odd_sum = 0;

    cout << "Enter a sequence of numbers (space separated): ";
    for (string s; getline(cin, s)) {
        float num = stof(s);
        lst.push_back(num);
        if (num > 0 && floor(num) == num) {
            if (num % 2 != 0)
                odd_sum += pow(num, 2);
        }
    }

    cout << "Double the difference: " << double_the_difference(lst) - 2 * odd_sum << endl;

    return 0;
}