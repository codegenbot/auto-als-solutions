#include <iostream>
#include <vector>
#include <cmath>

int sum_squares(std::vector<int> lst) {
    int result = 0;
    for (int i = 0; i < lst.size(); i++) {
        if ((i+1)%3 == 0 && (i+1)%4 != 0) {
            result += lst[i] * lst[i];
        } else if ((i+1)%4 == 0 && (i+1)%3 != 0) {
            result += pow(lst[i], 3);
        }
    }
    return result;
}

int main() {
    std::vector<int> input;
    int num;
    
    // Input values
    std::cout << "Enter the number of elements: ";
    int n; std::cin >> n;
    for(int i = 0; i < n; ++i) {
        std::cout << "Enter element " << (i+1) << ": ";
        std::cin >> num;
        input.push_back(num);
    }
    
    // Test the function
    int output = sum_squares(input);
    std::cout << "The sum of squares is: " << output << std::endl;

    return 0;
}