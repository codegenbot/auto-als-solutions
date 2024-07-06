```cpp
#include <string>
#include <iostream>

std::string fix_spaces(const std::string& str) {
    std::string result = " ";
    for (char c : str) {
        if (c == ' ') {
            if (!result.empty() && result.back() == ' ')
                continue;
        }
        result += c;
    }
    return result;
}

int main() {
    std::string str = " Example   3";
    cout << fix_spaces(str) << endl;
}