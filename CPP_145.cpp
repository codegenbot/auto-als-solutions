#include <algorithm>
#include <vector>
#include <initializer_list>

bool same(std::vector<int> a, std::vector<int> b) {
    return (a.size() == b.size()) && (std::equal(a.begin(), a.end(), b.begin()));
}

auto comp = [](int a, int b) {
    int sumA = 0, sumB = 0;
    for (char c : std::to_string(a)) sumA += c - '0';
    for (char c : std::to_string(b)) sumB += c - '0';
    if (sumA == sumB)
        return true;  
    return sumA < sumB;
};

std::vector<int> sortByPoints(const std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end(), comp);
    return nums;
}

int main() {
    assert(same(sortByPoints({0,6,6,-76,-21,23,4}), {-76, -21, 0, 4, 23, 6, 6}));
    return 0;
}