#include <iostream>
#include <vector>

std::vector<int> pluck(std::vector<int> arr) {
    std::vector<int> result;
    if (arr.empty()) {
        return result;
    }
    
    int smallest_even = INT_MAX;
    int index = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < smallest_even) {
            smallest_even = arr[i];
            index = i;
        }
    }
    
    result.push_back(smallest_even);
    result.push_back(index);
    
    return result;
}

int main() {
    std::vector<int> input;
    // Use the function
    std::cout << "Enter some numbers (separated by spaces): ";
    int n;
    while (std::cin >> n) {
        input.push_back(n);
        if (std::cin.peek() != ' ') {
            break;
        }
        std::cin.ignore();
    }
    
    std::vector<int> output = pluck(input);
    
    if (!output.empty()) {
        std::cout << "Smallest even number: " << output[0] << std::endl;
        std::cout << "Index of smallest even number: " << output[1] << std::endl;
    } else {
        std::cout << "No even numbers in the array." << std::endl;
    }
    
    return 0;
}