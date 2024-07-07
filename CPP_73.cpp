#include <vector>
#include <cassert>

int smallest_change(std::vector<int> arr) {
    int left = 0, right = arr.size() - 1;
    int changes = 0;

    while (left < right) {
        if (arr[left] != arr[right]) {
            changes++;
            break;
        }
        left++;
        right--;
    }

    for (int i = left; i <= right; i++) {
        if (arr[i] != arr[2 * right - i + 1])
            changes++;
    }

    return changes;
}

int main() {
    assert(smallest_change({0, 1}) == 1);
    return 0;
}