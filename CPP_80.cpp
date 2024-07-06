#include <string>
using namespace std;

bool is_happy(string s) {
    int n = s.length();
    if (n < 3)
        return false;
    for (int i = 0; i <= n - 3; i += 3) {
        string substr = s.substr(i, 3);
        bool unique = true;
        for (char c : substr) {
            int count = 0;
            for (int j = i; j < i + 3; j++) {
                if (s[j] == c)
                    count++;
            }
            if (count > 1) {
                unique = false;
                break;
            }
        }
        if (!unique)
            return false;
    }
    return true;
}

int main() {
    assert(is_happy("iopaxioi") == false );
    return 0;
}