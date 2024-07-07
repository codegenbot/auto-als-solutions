#include <vector>
#include <algorithm>
#include <string>

std::string find_max(std::vector<std::string> words){
    std::string max_word = *max_element(words.begin(), words.end(), 
                                   [](const std::string& a, const std::string& b) {
                                       return count(a.begin(), a.end(), a[0]) > count(b.begin(), b.end(), b[0]);
                                   });
    return max_word;
}