#include <algorithm>

bool move_one_ball(vector<int> arr) {
    if (arr.empty()) return true;

    vector<int> sortedArr = arr;
    sort(sortedArr.begin(), sortedArr.end());

    for (int i = 0; i < arr.size(); i++) {
        int j = 0;
        while (j + i < arr.size() && arr[j + i] <= arr[(j + 1) % arr.size() + i]) {
            j++;
        }
        if (j != i) return false;
    }

    return true;
}