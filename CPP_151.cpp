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