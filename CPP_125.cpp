#include <vector>
#include <string>

bool issame(const std::pair<std::vector<std::string>, std::vector<std::string>>& input) {
    if (input.first.size() != input.second.size()) return false;
    for (int i = 0; i < input.first.size(); ++i) {
        if (issame(input.first[i], input.second[i])) return false;
    }
    return true;
}

std::vector<std::string> split_words(std::string txt) {
    std::vector<std::string> result;
    size_t pos = 0;
    while ((pos = txt.find(' ')) != std::string::npos) {
        result.push_back(txt.substr(0, pos));
        txt.erase(0, pos + 1);
    }
    if (txt.empty()) return result;
    result.push_back(txt);
    return result;
}

int main() {
    std::string user_input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, user_input);

    std::vector<std::string> words = split_words(user_input);
    
    for (const auto& word : words) {
        std::cout << word << std::endl;
    }
}