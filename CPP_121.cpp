#include <iostream>

int sumOfAllOdd(int* nums, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) { 
        if (*(nums + i) % 2 != 0) {
            sum += *(nums + i);
        }
    }
    return sum;
}

int main() {
    int nums[4] = {3, 13, 2, 9};
    std::cout << sumOfAllOdd(nums, 4) << std::endl;
}