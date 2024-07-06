#include <iostream>
#include <vector>

int sumOfAllOdd(int* nums, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) { 
        if (*nums % 2 != 0) {
            sum += *nums;
        }
        nums++;
    }
    return sum;
}

int main() {
    std::cout << sumOfAllOdd({3, 13, 2, 9}, 4) << std::endl;
}