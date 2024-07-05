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
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    for(int i=0; i<n; i++) {
        float num;
        std::cout << "Enter element #"<<i+1<<": ";
        std::cin >> num;
        numbers.push_back(num);
    }
    float result = median(numbers);
    std::cout << "Median: "<<result<<std::endl;
    return 0;
}