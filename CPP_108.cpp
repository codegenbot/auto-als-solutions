#include<vector>
using namespace std;

int count_nums(vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (num >= 0) {
            int sum = 0;
            bool sign = false;
            for (long long temp = abs(num); temp > 0; temp /= 10) {
                if (sign)
                    sum -= temp % 10;
                else
                    sum += temp % 10;
                sign = !sign;
            }
            if (sum > 0) {
                count++;
            }
        }
    }
    return count;
}