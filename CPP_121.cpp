```cpp
#include <iostream>
#include <vector>

int sumOdd(int x) {
    int sum = 0;
    std::vector<int> vec(10); 

    for (int i = 1; i <= 10; i++) { 
        std::cin >> vec[i - 1]; 
    }

    for (int y : vec) {
        if (y % 2 != 0) {
            sum += y;
        }
   }
    
    return sum;
}

int main() {
    std::cout << sumOdd(0) << std::endl; 
    return 0;
}