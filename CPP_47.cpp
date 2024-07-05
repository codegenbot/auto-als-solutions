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
    int num_elements;
    std::cout << "Enter the number of elements: ";
    std::cin >> num_elements;
    
    for(int i=0; i<num_elements; ++i) {
        float element;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> element;
        numbers.push_back(element);
    }
    
    float result = median(numbers);
    std::cout << "Median: " << result << "\n";
    return 0;
}