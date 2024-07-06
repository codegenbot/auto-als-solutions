```cpp
#include <vector>
#include <algorithm>
#include <functional>

bool issame(std::vector<int> a, std::vector<int> b) {
    std::vector<int> res = a;
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
    return res == b;
}

int main() {
    std::vector<int> order_by_points = {0,6,6,-76,-21,23,4};
    assert(issame(order_by_points, {-76, -21, 0, 4, 23, 6, 6}));
    return 0;
}