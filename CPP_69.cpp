#include <algorithm>
#include <vector>

int findMaxValue(std::vector<int> numbers) {
    int maxValue = *std::max_element(numbers.begin(), numbers.end());
    return maxValue;
}

int main() {
    std::vector<int> numbers;
    int num;
    while (true) {
        std::cout << "Enter a number (or -1 to stop): ";
        std::cin >> num;
        if (num == -1) break;
        numbers.push_back(num);
    }
    int maxValue = findMaxValue(numbers);
    std::cout << "The maximum value is: " << maxValue << std::endl;
    return 0;
}