#include <algorithm>
#include <cmath>

int maximumAbsoluteDifference(vector<int> l) {
    int res = 0;
    std::vector<int> temp(l);
    std::sort(temp.begin(), temp.end());
    if (temp.size() > 1)
        res = std::abs(temp[temp.size()-1] - temp[0]);
    return res;
}