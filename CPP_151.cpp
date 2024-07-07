#include <iostream>
#include <vector>
#include <cmath>

std::vector<float> readInput() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    std::vector<float> lst(n);
    
    for (int i = 0; i < n; i++) {
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> lst[i];
    }
    
    return lst;
}

long long doubleTheDifference(const std::vector<float>& lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && modf(num, &num) == 0) {
            sum += pow(num, 2);
        }
    }
    
    return sum;
}

int main() {
    std::vector<float> lst = readInput();
    long long result = doubleTheDifference(lst);
    
    std::cout << "Double the difference: " << result << std::endl;
    
    return 0;
}