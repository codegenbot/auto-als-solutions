#include <vector>
using namespace std;

int smallest_change(vector<int> arr) {
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
        if (arr[i] != arr[(right - left + 1) - (i - left)]) {
            changes++;
        }
    }

    return changes;
}

int main() {
    assert(smallest_change({0, 1}) == 1);
    // Add your test cases here
    return 0;
}