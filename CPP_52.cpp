```cpp
#include <vector>

bool below_threshold(vector<int> l, int t) {
    for (int num : l) {
        if (num >= t) {
            return false;
        }
    }
    return true;

}

int main() {
    assert(!below_threshold({1, 8, 4, 10}, 10));
    vector<int> numbers = {5, 3, 8};
    int threshold = 6;
    if (below_threshold(numbers, threshold)) {
        cout << "All elements are below the threshold." << endl;
    } else {
        cout << "At least one element is not below the threshold." << endl;
    }
    return 0;
}