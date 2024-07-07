#include <vector>

std::vector<int> leaders(std::vector<int> v) {
    std::vector<int> result;
    int maxRight = v.back();
    for (int i = v.size() - 1; i >= 0; --i) {
        if (v[i] >= maxRight) {
            result.push_back(v[i]);
            maxRight = v[i];
        }
    }
    return result;
}