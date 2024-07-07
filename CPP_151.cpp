#include <cmath>
#include <vector>

int main() {
    std::vector<float> lst;
    float num;
    int count = 0;

    while (std::cin >> num) {
        lst.push_back(num);
    }

    long long sum = 0;
    for (float n : lst) {
        if (n > 0 && floor(n) == n) {
            sum += pow(n, 2);
        }
    }
    std::cout << sum << std::endl;

    return 0;
}