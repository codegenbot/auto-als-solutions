#include <iostream>
#include <string>

std::string spinWords(std::string str) {
    std::string result = "";
    int start = 0;
    
    for (int i = 0; i <= str.length(); i++) {
        if (i == str.length() || str[i] == ' ') {
            if (i - start >= 5) {
                std::reverse(str.substr(start, i - start).begin(), str.substr(start, i - start).end());
            }
            result += str.substr(start, i - start);
            if (i < str.length()) {
                result += " ";
            }
            start = i + 1;
        }
    }
    
    return result;
}

int main() {
    std::cout << spinWords("a") << std::endl; // a
    std::cout << spinWords("this is a test") << std::endl; // this is a test
    std::cout << spinWords("this is another test") << std::endl; // this is rehtona test
    std::cout << spinWords("hi") << std::endl; // hi
    
    return 0;
}