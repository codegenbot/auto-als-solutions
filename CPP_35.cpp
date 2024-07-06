#include <algorithm>
#include <cmath>

int findMax(int n) {
    std::vector<int> l;
    for (int i = 0; i <= n; i++) {
        int num;
        std::cout << "Enter number: ";
        std::cin >> num;
        l.push_back(num);
    }
    
    return *std::max_element(l.begin(), l.end());
}