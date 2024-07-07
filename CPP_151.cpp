#include <cmath>
#include <vector>

int main() {
    std::vector<float> lst;
    for (int i = 0; i < 5; i++) {
        float num;
        std::cout << "Enter number: ";
        std::cin >> num;
        lst.push_back(num);
    }

    long long double_the_difference = double_the_difference(lst);
    assert(double_the_difference == 14); 
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