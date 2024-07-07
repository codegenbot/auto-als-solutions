```cpp
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
    std::vector<int> testVector;
    int n, k;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    testVector.resize(n);
    for (int i = 0; i < n; i++) {
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> testVector[i];
    }
    std::cout << "Enter the value of k: ";
    std::cin >> k;
    int result = add_elements(testVector, k);
    std::cout << "The sum is: " << result << std::endl;
    return 0;
}