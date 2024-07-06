#include <iostream>
#include <vector>

int main(std::vector<int> lst) {
    int sum = 0;
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    std::cout << "Error: Please enter valid input." << std::endl;
    return -1;
}