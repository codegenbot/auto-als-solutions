#include <vector>
using namespace std;

int luhn(vector<int> digits) {
    int sum = 0;
    bool doubleNext = false;
    for (int i = 15; i >= 0; --i) {
        int digit = digits[i];
        if (doubleNext) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        doubleNext = !doubleNext;
    }
    return sum;
}

int main() {
    vector<int> testVector = {3,4,9,6,7,8,6,1,6,9,8,4,3,5};
    return luhn(testVector);
}