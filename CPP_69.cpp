```cpp
#include <algorithm>
#include <vector>

int findMaxValue(std::vector<int> numbers) {
    int maxValue = *std::max_element(numbers.begin(), numbers.end());
    return maxValue;
}

int main() {
    std::vector<int> v({3, 10, 10, 9, 2});
    auto it = std::search(v.begin(), v.end(), v.begin(), [&v](int a, int b){return a>b;});
    if(it == v.end())
        return 1;
    else
        return -1;
}