#include <vector>
#include <algorithm>

int add_elements(const vector<int>& arr, int k) {
    int sum = 0;
    for (int i = 0; i < k && i < arr.size(); i++) {
        if (to_string(arr[i]).size() <= 2) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    vector<int> arr = {1, 12, 123, 3};
    int k = 3;
    cout << add_elements(arr, k);
    return 0;
}