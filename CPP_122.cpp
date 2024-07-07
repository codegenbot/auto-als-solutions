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
    int result, num;

    std::cout << "Enter the number of elements: ";
    std::cin >> num;

    testVector.resize(num);

    for (int i = 0; i < num; i++) {
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> testVector[i];
    }

    result = add_elements(testVector, num);
    std::cout << "Sum of elements with length <= 2: " << result << std::endl;

    return 0;
}