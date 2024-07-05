#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

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
    float input;
    
    // Read inputs from user
    while (true) {
        std::cout << "Enter a number (-1 to finish): ";
        std::cin >> input;
        if (input == -1) break;
        numbers.push_back(input);
    }
    
    float result = median(numbers);
    assert(std::abs(result - 7.0f) < 1e-4); 
    return 0;
}