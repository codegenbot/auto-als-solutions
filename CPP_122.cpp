#include<vector>

int add_elements(std::vector<int> arr, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
        if (to_string(arr[i]).length() <= 2) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> testVector = {1};
    int result = add_elements(testVector, 1);
    return 0;
}