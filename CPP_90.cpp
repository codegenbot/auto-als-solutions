#include <vector>
#include <limits>

int next_smallest(std::vector<int> lst) {
    if (lst.empty()) return 0;
    int result = lst[0];
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] <= result) {
            result = lst[i];
        }
    }
    return result;
}