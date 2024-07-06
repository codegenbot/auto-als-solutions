#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    std::string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (text[i] == ' ' && (i == 0 || text[i-1] != ' ') && (i == text.length()-1 || text[i+1] != ' ')) {
            result += "_";
        } else if (text[i] == ' ') {
            bool consecutive = true;
            for (int j = i + 1; j < text.length() && j > 0; j++) {
                if (text[j] == ' ') {
                    consecutive = false;
                    break;
                }
            }
            if (consecutive) {
                result += "-";
            } else {
                result += "_";
            }
        } else {
            result += text[i];
        }
    }
    return result;
}

int main() {
    std::string text;
    std::cout << "Enter a string: ";
    std::getline(std::cin, text);
    std::cout << "Fixed string: " << fix_spaces(text) << std::endl;
    return 0;
}