```cpp
#include <cassert>

int multiply(int a, int b) {
    if(a < 10 && b < 10)
        return (a * 10 + b) * (a * 10 + b);
    else 
        return (a % 10) * (b % 10);
}

assert(multiply(0, 0) == 0);