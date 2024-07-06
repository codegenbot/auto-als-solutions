#include <vector>
#include <string>
#include <algorithm>

bool will_it_fly(std::vector<int> q, int w) {
    std::string s = "";
    for (int i : q) {
        s += std::to_string(i);
    }
    if (!isPalindrome(s)) {
        return false;
    }
    int sum = 0;
    for (int i : q) {
        sum += i;
    }
    return sum <= w;
}

bool isPalindrome(std::string s) {
    std::string t = s;
    std::reverse(t.begin(), t.end());
    return s == t;
}

int main() {
    assert(will_it_fly({5}, 5) == true);
    return 0;
}