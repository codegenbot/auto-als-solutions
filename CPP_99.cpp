Here is the solution:

```cpp
#include <string>
#include <cmath>

int closest_integer(string value) {
    double num = stod(value);
    if (num - static_cast<int>(num) < static_cast<int>(num) - num) {
        return static_cast<int>(num + 0.5);
    } else {
        return static_cast<int>(num);
    }
}