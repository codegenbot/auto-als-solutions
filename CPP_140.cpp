```cpp
#include <string>
#include <iostream>

std::string fix_spaces(const std::string& str) {
    int i = 0;
    int j = 0;

    while (j < str.length()) {
        if ((str[j] == ' ') && (i > 0) && (str[i-1] == ' ')) {
            j++;
        } else {
            str[i++] = str[j++];
        }
    }

    return str.substr(0, i);
}

int main() {
    std::string str = " Example   3";
    cout << fix_spaces(str) << endl;
}