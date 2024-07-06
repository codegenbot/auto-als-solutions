#include <vector>
#include <algorithm>
#include <set>

std::vector<int> sortByDigitSum(std::vector<int> arr) {
    sort(arr.begin(), arr.end(), [](int a, int b)->bool{
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

int main() {
    std::vector<int> arr = {0, 6, 6, -76, -21, 23, 4};
    std::vector<int> sortedArr = sortByDigitSum(arr);
    
    for (int i : sortedArr) {
        std::cout << i << " ";
    }
    return 0;
}