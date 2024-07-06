#include <string>
#include <vector>
#include <algorithm>

std::string find_max(std::vector<std::string> words) {
    std::string max_word = *max_element(words.begin(), words.end(),
        [](const std::string& s1, const std::string& s2) {
            if (s1.length() == s2.length()) {
                return s1 < s2;
            }
            return s1.length() > s2.length();
        });
    return max_word;
}