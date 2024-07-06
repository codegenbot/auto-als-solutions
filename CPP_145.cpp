```cpp
#include <algorithm>
#include <vector>

bool issame(int a, int b) {
    long long sum1 = 0, sum2 = 0;
    while(a > 0){
        sum1 += a % 10;
        a /= 10;
    }
    while(b > 0){
        sum2 += b % 10;
        b /= 10;
    }
    return (sum1 == sum2);
}

std::vector<int> sortByDigitSum(std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(), [&](int a, int b)->bool{
        if (!issame(a,b)) return (long long)(a) < (long long)(b);
        else return (long long)(a) < (long long)(b);
    });
    return arr;
}