```cpp
#include <vector>
#include <string>
#include <initializer_list>

bool issame(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    return a == b;
}

std::vector<std::string> split_words(string txt) {
    vector<string> result;
    size_t pos = 0;
    while ((pos = txt.find(' ')) != string::npos) {
        result.push_back(txt.substr(0, pos));
        txt.erase(0, pos + 1);
    }
    if (txt.empty()) {
        return result;
    }
    result.push_back(txt);
    return result;
}

int main() {
    #define _CRT_SECURE_NO_WARNINGS
    std::string user_input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, user_input);

    std::vector<std::string> words = split_words(user_input);
    
    for (const auto& word : words) {
        std::cout << word << std::endl;
    }
}