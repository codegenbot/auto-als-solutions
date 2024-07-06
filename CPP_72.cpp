#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool will_it_fly(vector<int> q, int w) {
    string str = "";
    for (int i : q) {
        str += to_string(i);
    }
    long long sum = 0;
    for (int i : q) {
        sum += i;
    }
    bool isRevSumPalindrome = false;
    long long revSum = 0;
    while(sum > 0) {
        revSum = 0;
        int temp = sum;
        while(temp > 0) {
            revSum = revSum * 10 + temp % 10;
            temp /= 10;
        }
        if(revSum == sum) {
            isRevSumPalindrome = true;
            break;
        }
        sum = revSum;
    }
    return (isRevSumPalindrome && stoll(str) <= w);
}

bool isPalindrome(string s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    return s == rev;
}

int main() {
    assert(will_it_fly({5}, 5) == true);
    return 0;
}