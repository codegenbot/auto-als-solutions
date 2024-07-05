```
#include <iostream>
#include <vector>
#include <algorithm>

float median(std::vector<float> l) {
    std::sort(l.begin(), l.end());
    int n = l.size();
    if (n % 2 == 0) {
        return ((l[n / 2 - 1] + l[n / 2]) / 2.0);
    } else {
        return l[n / 2];
    }
}

int main() {
    std::vector<float> numbers;
    int numInput = 0;

    std::cout << "Enter the number of inputs: ";
    std::cin >> numInput;

    for (int i = 0; i < numInput; ++i) {
        float input;
        std::cout << "Enter input " << i + 1 << ": ";
        std::cin >> input;
        numbers.push_back(input);
    }

    float result = median(numbers);

    std::cout << "Median: " << result << std::endl;

    return 0;
}