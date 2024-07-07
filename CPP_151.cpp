#include <cmath>
#include <vector>

int main() {
    std::vector<float> lst;
    float num;
    while(std::cin >> num) {
        lst.push_back(num);
    }

    long long double_the_difference = 0;
    for (float n : lst) {
        if (n > 0 && floor(n) == n) {
            double_the_difference += pow(n, 2);
        }
    }
    std::cout << double_the_difference;
    return 0;
}