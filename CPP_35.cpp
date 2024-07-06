#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> l;
    int n;
    std::cout << "Enter number of elements: ";
    std::cin >> n;
    for(int i=0; i<n; i++){
        int x;
        std::cout << "Enter element " << (i+1) << ": ";
        std::cin >> x;
        l.push_back(x);
    }
    return *std::max_element(l.begin(), l.end());
}