#include <iostream>
#include <vector>
#include <cmath>

long long doubleTheDifference(std::vector<float> numbers) {
    long long sum = 0;
    for (float num : numbers) {
        if (num > 0 && modf(num, &num) == 0) {
            sum += pow(num, 2);
        }
    }
    return sum;
}

int main() {
    std::vector<float> numbers;
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        float num;
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> num;
        numbers.push_back(num);
    }
    long long result = doubleTheDifference(numbers);
    std::cout << "Double the difference: " << result << std::endl;
    return 0;
}