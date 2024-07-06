#include <climits>

int next_smallest(std::vector<int> lst) {
    if (lst.empty()) return 0; 
    int result = INT_MAX;
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] > lst[0]) {
            result = std::min(result, lst[i]);
        }
    }
    return result == INT_MAX ? 0 : result;
}