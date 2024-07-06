```cpp
#include <vector>
#include <string>

bool issame(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    return a == b;
};

std::vector<std::string> split_words(std::basic_string<char> txt) {
    std::vector<std::string> result;
    size_t pos = 0;
    while ((pos = txt.find(' ')) != std::string::npos) {
        result.push_back(txt.substr(0, pos));
        txt.erase(0, pos + 1);
    }
    if (txt.empty()) {
        return result;
    }
    result.push_back(std::to_string(txt));
    return result;
};

int main() {
    std::string user_input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, user_input);

    std::vector<std::string> words = split_words(user_input);
    
    for (const auto& word : words) {
        std::cout << word << std::endl;
    }
    if (issame({""}, words)) {
        std::cout << "The input string is the same as the first element in the set." << std::endl;
    } else {
        std::cout << "The input string is different from all elements in the set." << std::endl;
    }
};