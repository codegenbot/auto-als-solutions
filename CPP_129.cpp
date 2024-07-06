#include <vector>

int minPath(std::vector<std::pair<int, int>>& path) {
    if (path.empty()) return -1;

    int min = INT_MAX;
    for (auto it = path.begin(); it != path.end(); ++it) {
        int sum = 0;
        for (int i = 0; i < 2; ++i)
            sum += it->first * (1 << i);
        if (sum < min)
            min = sum;
    }
    return min;
}

bool isEqual(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}