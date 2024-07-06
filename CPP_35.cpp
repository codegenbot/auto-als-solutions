#include <algorithm>
#include <cmath>
#include <vector>

int max_abs(int n) {
    std::vector<int> l;
    for (int i = 0; i < n; i++) {
        int input;
        std::cin >> input;
        l.push_back(input);
    }
    
    return *std::max_element(l.begin(), l.end());
}