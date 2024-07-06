```cpp
#include <vector>
#include <algorithm>

bool below_threshold(const std::vector<int>& l, int t) {
    return std::all_of(l.begin(), l.end(), [t](int i){return i < t;});
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> l(n);
    for (auto& x : l)
        std::cin >> x;
    int t;
    std::cin >> t;
    if (below_threshold(l, t)) {
        std::cout << "True" << std::endl;
    } else {
        std::cout << "False" << std::endl;
    }
    return 0;
}