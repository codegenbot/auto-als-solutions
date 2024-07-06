#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> l;
    // Ask user for input
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    // Add 'n' number of elements to the vector
    for(int i = 0; i < n; i++) {
        int x;
        std::cout << "Element #"<<i+1<<": ";
        std::cin >> x;
        l.push_back(x);
    }

    // Find and return the maximum element from the vector
    if(!l.empty())
        return *max_element(l.begin(), l.end());
    else
        return -1; // or handle this case as you like

    return 0;
}