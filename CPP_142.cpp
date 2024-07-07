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
    std::vector<int> lst;
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> x;
        lst.push_back(x);
    }
    int output = sum_squares(lst);
    std::cout << "Sum of squares: " << output << std::endl;
    return 0;
}