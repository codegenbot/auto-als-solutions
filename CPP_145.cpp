#include <vector>
#include <algorithm>
#include <set>

std::vector<int> sortByDigitSum(std::vector<int> arr) {
    std::vector<int> res;
    for (int i : arr) {
        res.push_back(i);
    }
    sort(res.begin(), res.end(), [](int a, int b)->bool{
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
    return res;
}