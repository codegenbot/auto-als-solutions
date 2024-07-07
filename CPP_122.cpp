```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int k;
    std::vector<int> arr;
    std::cout << "Enter the size of array: ";
    std::cin >> k;
    for (int i = 0; i < k; i++) {
        int num;
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> num;
        arr.push_back(num);
    }
    int sum = add_elements(arr, k);
    std::cout << "The sum of elements is: " << sum << std::endl;
    return 0;
}

int add_elements(vector<int> arr, int k) {
    int sum = 0;
    for (int i = 0; i < min(k, arr.size()); i++) {
        if (to_string(arr[i]).size() <= 2) {
            sum += arr[i];
        }
    }
    return sum;
}