#include <stdio.h>
#include <vector>
using namespace std;

vector<int> tri(int n) {
    vector<int> result;
    if (n == 0) return result;
    result.push_back(3);
    if (n > 1) {
        if (n % 2 == 0) {
            for (int i = 1; i <= n / 2; i++) {
                result.push_back(i * 2 + 1);
            }
        } else {
            result.push_back(1);
            int prev1 = 3, prev2 = 1;
            for (int i = 2; i < n; i++) {
                result.push_back(prev1 + prev2 + 1);
                if (i % 2 == 0) prev2 = result.back();
                else {
                    prev1 = result.back();
                    prev2 = prev1 - 3;
                }
            }
        }
    }
    return result;
}