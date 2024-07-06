#include <string>

int correct_bracketing(string brackets) {
    int count = 0;
    for (char c : brackets) {
        if (c == '(') {
            count++;
        } else if (c == ')') {
            if (count == 0)
                return 0; // Wrong bracketing
            count--;
        }
    }
    if(count != 0)
        return 0; // Wrong bracketing
    return 1; // Correct bracketing
}