#include <vector>
#include <algorithm>
#include <string>

int add_elements(const std::vector<int>& arr, int k) {
    int sum = 0;
    for (int i = 0; i < k && i < arr.size(); i++) {
        if (std::to_string(arr[i]).size() <= 2) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    // Test the function
    std::vector<int> input;
    int count;
    std::cout << "Enter the elements of array: ";
    for(int i = 0; i < 10; i++) {
        int num;
        std::cin >> num;
        input.push_back(num);
    }
    std::cout << "Enter the number of elements to add: ";
    std::cin >> count;
    std::cout << "The sum is: " << add_elements(input, count) << std::endl;
}