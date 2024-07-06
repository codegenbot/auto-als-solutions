```cpp
#include <cmath>
int digits(int n){
    int product = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= (int)pow(digit, 2);
        }
        n /= 10;
    }
    return product;
}