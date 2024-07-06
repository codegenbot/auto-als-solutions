```
#include <algorithm>
#include <vector>

bool issame(std::vector<int> a, std::vector<int> b) {
    return (a.size() == b.size()) && (std::equal(a.begin(), a.end(), b.begin()));
}

namespace std;
std::vector<int> order_by_points(std::vector<int> nums) {
    auto comp = [&nums](int a, int b) {
        int sumA = 0, sumB = 0;
        for (char c : to_string(a)) sumA += c - '0';
        for (char c : to_string(b)) sumB += c - '0';
        if (sumA == sumB)
            return nums.find(a) > nums.find(b);
        return sumA < sumB;
    };
    sort(nums.begin(), nums.end(), comp);
    return nums;
}

int main2() {
    assert(issame(order_by_points({0,6,6,-76,-21,23,4}) , {-76, -21, 0, 4, 23, 6, 6}));
    return 0;
}