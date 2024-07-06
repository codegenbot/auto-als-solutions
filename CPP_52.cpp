#include <vector>
bool below_threshold(vector<std::int32_t> l, int t) {
    for (int num : l) {
        if (num >= t) {
            return false;
        }
    }
    return true;
}