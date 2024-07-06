#include <vector>
#include <algorithm>

std::vector<float> get_positive(std::vector<float> l) {
    std::vector<float> positive;
    for (float x : l) {
        if (x > 0) {
            positive.push_back(x);
        }
    }
    return positive;
}