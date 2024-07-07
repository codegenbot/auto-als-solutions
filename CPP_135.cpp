#include <vector>
int can_arrange(vector<int> arr) {
    int i = -1;
    for (int j = 0; j < arr.size() - 1; j++) {
        if (arr[j] >= arr[j + 1]) {
            return j + 1;
        }
    }
    return arr.size();
}