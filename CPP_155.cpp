Here is the solution:

```cpp
#include <vector>

vector<int> even_odd_count(int num) {
    vector<int> result(2);
    int n = abs(num); // remove sign bit if present
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 == 0)
            result[0]++;
        else
            result[1]++;
        n /= 10;
    }
    return result;
}