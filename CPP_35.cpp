#include <algorithm>
#include <cmath>
#include <vector>

int findMax(int n) {
    std::vector<int> l;
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        l.push_back(num);
    }
    
    return *std::max_element(l.begin(), l.end());
}