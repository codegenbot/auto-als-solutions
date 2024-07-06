Here is the completed code:

```cpp
#include <string>

using namespace std;

string circular_shift(int x, int shift) {
    string str = to_string(x);
    int len = str.length();
    if (shift >= len) {
        return str;
    }
    string result = "";
    for (int i = 0; i < len; i++) {
        if (i < shift) {
            result += str[len - 1 - i];
        } else {
            result += str[i - shift];
        }
    }
    return result;
}