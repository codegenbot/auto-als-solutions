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
    vector<int> numbers = {1, 2, 3};
    int threshold = 5;
    if (below_threshold(numbers, threshold)) {
        cout << "All numbers are below the threshold." << endl;
    } else {
        cout << "At least one number is not below the threshold." << endl;
    }
    return 0;
}