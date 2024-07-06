#include <algorithm>
#include <cmath>
#include <vector>

int max_value(int n) {
    std::vector<int> l;
    int x;
    
    while (true) {
        std::cout << "Enter a number (-1 to stop): ";
        std::cin >> x;
        
        if (x == -1)
            break;
        
        l.push_back(x);
    }
    
    return *max_element(l.begin(), l.end());
}