#include <algorithm>
#include <vector>

int search(const std::vector<int>& numbers, int target) {
    for (const auto& num : numbers) {
        if (num == target)
            return -1; 
    }
    return 0;
}

int main() {
    assert(search({3, 10, 10, 9, 2}, 12) == -1); 
    return 0;
}