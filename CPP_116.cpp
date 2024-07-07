#include <iostream>
#include <vector>
#include <algorithm>

// Function to count the number of 1 bits in a binary number
bool issame(std::vector<int> a, std::vector<int> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); ++i)
        if (a[i] != b[i]) return false;
    return true;
}

// Function to sort the array based on the number of 1 bits in binary representation
std::vector<int> sort_array(std::vector<int> arr) {
    std::vector<std::pair<int, int>> result;
    for (int i : arr) {
        int ones = 0;
        int num = i;
        while (num > 0) {
            if ((num & 1) == 1)
                ones++;
            num >>= 1;
        }
        result.push_back({ones, i});
    }
    std::sort(result.begin(), result.end());
    std::vector<int> res;
    for (auto x : result) {
        res.push_back(x.second);
    }
    return res;
}

int main() {
    assert(issame(sort_array({2, 4, 8, 16, 32}), {2, 4, 8, 16, 32}));
    std::cout << "Test passed." << std::endl;
    return 0;
}