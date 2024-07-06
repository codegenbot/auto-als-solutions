#include <vector>

int smallest_change(vector<int> arr) {
    int n = arr.size();
    int changes = 0;

    for (int i = 1; i < n; i++) {
        if (arr[i - 1] > arr[i]) {
            changes++;
            while (i < n && arr[i - 1] > arr[i]) {
                i++;
            }
        }
    }

    return changes;
}

int main() {
    assert (smallest_change({0, 1}) == 1);
    // ...
}