Here is the completed code:

```cpp
#include <string>
using namespace std;

string fix_spaces(string text) {
    for (int i = 0; i < text.length(); i++) {
        if (text[i] == ' ') {
            int count = 1;
            while (i + count < text.length() && text[i + count] == ' ') {
                count++;
            }
            string temp = "";
            temp += text.substr(0, i);
            if (count > 2) {
                temp += "-";
            } else {
                for (int j = 1; j < count; j++) {
                    temp += "_";
                }
            }
            temp += text.substr(i + count);
            return temp;
        }
    }
    return text;
}