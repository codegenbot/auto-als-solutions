#include <algorithm>
#include <vector>

int findMaxValue(std::vector<int> numbers) {
    int maxValue = *std::max_element(numbers.begin(), numbers.end());
    return maxValue;
}

bool exists(const std::vector<int>& vec1, const std::vector<int>& vec2) {
    if (vec1.size() != vec2.size())
        return false;

    for (int i = 0; i < vec1.size(); ++i)
        if (vec1[i] != vec2[i])
            return false;
    
    return true;
}

int main() {
    std::vector<int> v1({3, 10, 10, 9, 2});
    int pos = -1;

    for (int i = 0; i < 1; ++i) {
        pos = std::search(v1.begin(), v1.end(), v1.begin(), v1.end() - 1) - v1.begin();
        if (pos != v1.size()) 
            break;
    }

    return 0;
}