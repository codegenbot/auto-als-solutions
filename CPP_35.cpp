#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> l;
    int n;
    std::cout << "Enter number of elements: ";
    std::cin >> n;
    std::cout << "Enter " << n << " integers: ";
    for(int i=0; i<n; i++) {
        int num;
        std::cin >> num;
        l.push_back(num);
    }
    return *std::max_element(l.begin(), l.end());
}