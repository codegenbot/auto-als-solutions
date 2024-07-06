#include <vector>
#include <algorithm>

std::vector<int> sortByDigitSum(std::vector<int> &arr) {
    std::sort(arr.begin(), arr.end(), [&](int a, int b)->bool{
        long long sum1 = 0, sum2 = 0;
        while(a > 0){
            sum1 += a % 10;
            a /= 10;
        }
        while(b > 0){
            sum2 += b % 10;
            b /= 10;
        }
        return sum1 < sum2;
    });
    return arr;
}

assert(std::equal(std::begin({0,6,6,-76,-21,23,4}), std::end({0,6,6,-76,-21,23,4}), std::begin({-76, -21, 0, 4, 23, 6, 6})));