```cpp
#include <string>

int correct_bracketing(string brackets) {
    int count = 0;
    for (char c : brackets) {
        if (c == '(') {
            count++;
        } else if (c == ')') {
            if (count == 0)
                return 0; // incorrect bracketing
            count--;
        }
    }
    if(count == 0) 
        return 1; // correct bracketing
    else
        return 2; // incomplete bracketing
}