```cpp
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

std::vector<int> sort_by_digit_sum(std::vector<int> arr) {
    std::vector<int> res = arr;
    std::sort(res.begin(), res.end(), [&](int a, int b)->bool{
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

int main() {
    std::vector<int> input = {0,6,6,-76,-21,23,4};
    auto res = sort_by_digit_sum(input);
    // process result
    return 0;
}