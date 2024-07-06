#include <stdio.h>
#include <string>
using namespace std;

bool is_happy(string s) {
    if (s.length() < 3)
        return false;
    for (int i = 0; i <= s.length() - 3; i++) {
        string t = s.substr(i, 3);
        bool duplicate = false;
        for (char c : t) {
            int count = 0;
            for (int j = i; j < i + 3 && j < s.length(); j++) {
                if (s[j] == c) {
                    count++;
                }
            }
            if (count > 1) {
                duplicate = true;
                break;
            }
        }
        if (!duplicate)
            return false;
    }
    return true;
}