#include <vector>

int can_arrange(std::vector<int> arr) {
    int first = -1;
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] <= arr[i - 1]) {
            if (first == -1)
                first = i;
            else
                return -1;
        }
    }
    return first;
}