#include <stdio.h>
#include <string>
using namespace std;

bool is_happy(string s) {
    if (s.length() < 3)
        return false;
    for (int i = 0; i <= s.length() - 3; i++) {
        string substr = s.substr(i, 3);
        int count = 0;
        bool flag = true;
        for (char c : substr) {
            if (count == 0)
                first_char = c;
            else if (c == first_char)
                flag = false;
            count++;
        }
        if (!flag)
            return false;
    }
    return true;
}