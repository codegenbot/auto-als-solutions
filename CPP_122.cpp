#include <iostream>
#include <vector>
#include <string>

int main() {
    int n;
    std::cout << "Enter number of elements: ";
    std::cin >> n;

    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> arr[i];
    }

    int k;
    std::cout << "Enter value of k: ";
    std::cin >> k;

    int sum = add_elements(arr, k);

    std::cout << "Sum of elements with size <= 2 is: " << sum << std::endl;

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