```cpp
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
    vector<int> numbers = {1, 10, 5, 3};
    int result = add_elements(numbers, 4);
    cout << "Sum of elements with size of representation less than or equal to 2: " << result << endl;
    return 0;
}