#include <iostream>
#include <vector>

int add_elements(std::vector<int> arr, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) {
        if (std::to_string(arr[i]).length() <= 2) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> my_array;
    int k;
    std::cout << "Enter the number of elements: ";
    std::cin >> k;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < k; i++) {
        int num;
        std::cin >> num;
        my_array.push_back(num);
    }
    std::cout << "The sum of elements with length of string representation <= 2 is: " << add_elements(my_array, k) << std::endl;
    return 0;
}