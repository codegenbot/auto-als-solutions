#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return (a.size() == b.size()) && (a == b);
}

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