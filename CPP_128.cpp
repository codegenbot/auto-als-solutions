#include <vector>

using namespace std;

int prod_signs(vector<int> arr) {
    int sign_product = 1;
    long sum_of_magnitudes = 0;
    
    for (int num : arr) {
        if (num == 0) {
            return -32768; // special case: product of all signs is 0
        }
        
        int sign = (num > 0 ? 1 : (num < 0 ? -1 : 0));
        sum_of_magnitudes += abs(num);
        sign_product *= sign;
    }
    
    return (arr.empty() ? -32768 : sign_product * sum_of_magnitudes);
}