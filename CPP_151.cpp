#include <cmath>
#include <vector>

int main() {
    std::vector<float> lst;
    float num;
    while (std::cin >> num) {
        lst.push_back(num);
    }

    long long double_the_difference = double_the_difference(lst);
    assert(double_the_difference == 0); // replace with correct calculation or value
    return 0;
}

long long double_the_difference(vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && floor(num) == num) {
            sum += pow(num, 2);
        }
    }
    return sum;
}