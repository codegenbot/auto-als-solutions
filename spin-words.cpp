#include <string>
#include <sstream>

std::string spinWords(const std::string& input) {
    std::stringstream ss(input);
    std::string word;
    std::stringstream result;

    while (ss >> word) {
        if (word.length() >= 5) {
            std::reverse(word.begin(), word.end());
        }
        result << word << " ";
    }

    return result.str().substr(0, result.str().size() - 1);
}