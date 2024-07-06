#include <algorithm>
#include <string>
#include <vector>

bool issame(std::vector<int> a, std::vector<int> b) {
    return (a.size() == b.size()) && (std::equal(a.begin(), a.end(), b.begin()));
}

std::vector<int> order_by_points(std::vector<int> nums) {
    auto comp = [&nums](int a, int b) {
        int sumA = 0, sumB = 0;
        std::string strA = std::to_string(a);
        std::string strB = std::to_string(b);
        for (char c : strA) sumA += c - '0';
        for (char c : strB) sumB += c - '0';
        if (sumA == sumB)
            return nums.find(a) > nums.find(b);
        return sumA < sumB;
    };
    std::sort(nums.begin(), nums.end(), comp);
    return nums;
}